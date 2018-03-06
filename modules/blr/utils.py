import imp
import logging
import os
import sys
from functools import partial
from pathlib import Path

import blender_async
import pyinotify

import blr

logger = logging.getLogger(__name__)

CUR_DIR = Path(os.path.dirname(os.path.abspath(__file__)))


def reload():
    logger.info('reload')
    try:
        for m in sys.modules:
            if not m.startswith('blr'):
                continue
            try:
                imp.reload(sys.modules[m])
            except Exception as e_reload:
                logger.warn("Can't reload %s: %s", m, e_reload)
    except Exception as e_iter:
        logger.warn('module iteration failed: %s', e_iter)


def reload_and_rebuild(context, notifier):
    reload()
    blr.cmd.rebuild(context)


class Watcher:

    __manager = None
    __notifier = None

    def watch(self, context):

        if self.__manager:
            return

        logger.info('start watching: %s', CUR_DIR)

        loop = blender_async.get_event_loop()

        self.__manager = pyinotify.WatchManager()
        self.__notifier = pyinotify.AsyncioNotifier(
            self.__manager,
            loop,
            callback=partial(reload_and_rebuild, context)
        )

        self.__manager.add_watch(str(CUR_DIR), pyinotify.IN_MODIFY)
        self.__manager.add_watch(str(CUR_DIR / 'parts'), pyinotify.IN_MODIFY)
