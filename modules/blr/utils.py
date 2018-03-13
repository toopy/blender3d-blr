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
    try:
        modules_to_reload = [
            m for m in sys.modules
            if m.startswith('blr')
        ]
        for m in sorted(modules_to_reload, reverse=True):
            try:
                imp.reload(sys.modules[m])
            except Exception as e_reload:
                logger.warn("Can't reload %s: %s", m, e_reload)
    except Exception as e_iter:
        logger.warn('module iteration failed: %s', e_iter)


def reload_and_rebuild(context, notifier, operator='blr_floor0'):
    reload()
    blr.cmd.rebuild(context, operator=operator)


class Watcher:

    __manager = None
    __notifier = None

    def watch(self, context, operator='blr_floor0'):

        if self.__manager:
            return

        logger.info('start watching: %s', CUR_DIR)

        loop = blender_async.get_event_loop()

        self.__manager = pyinotify.WatchManager()
        self.__notifier = pyinotify.AsyncioNotifier(
            self.__manager,
            loop,
            callback=partial(reload_and_rebuild, context, operator=operator)
        )

        self.__manager.add_watch(str(CUR_DIR),
                                 pyinotify.IN_MODIFY)
        self.__manager.add_watch(str(CUR_DIR / 'parts'),
                                 pyinotify.IN_MODIFY)
        self.__manager.add_watch(str(CUR_DIR / 'parts' / 'floor0_children'),
                                 pyinotify.IN_MODIFY)
        self.__manager.add_watch(str(CUR_DIR / 'parts' / 'floor0_children' / 'entry_children'),
                                 pyinotify.IN_MODIFY)
        self.__manager.add_watch(str(CUR_DIR / 'parts' / 'floor0_children' / 'fireplace_children'),
                                 pyinotify.IN_MODIFY)
        self.__manager.add_watch(str(CUR_DIR / 'parts' / 'floor0_children' / 'saloon_children'),
                                 pyinotify.IN_MODIFY)
        self.__manager.add_watch(str(CUR_DIR / 'parts' / 'floor0_children' / 'wood0_children'),
                                 pyinotify.IN_MODIFY)
        self.__manager.add_watch(str(CUR_DIR / 'parts' / 'floor2_children'),
                                 pyinotify.IN_MODIFY)
        self.__manager.add_watch(str(CUR_DIR / 'parts' / 'floor2_children' / 'canopy0_children'),
                                 pyinotify.IN_MODIFY)
        self.__manager.add_watch(str(CUR_DIR / 'parts' / 'floor2_children' / 'wall1_children'),
                                 pyinotify.IN_MODIFY)
        self.__manager.add_watch(str(CUR_DIR / 'parts' / 'floor2_children' / 'wall2_children'),
                                 pyinotify.IN_MODIFY)
        self.__manager.add_watch(str(CUR_DIR / 'parts' / 'floor2_children' / 'wall3_children'),
                                 pyinotify.IN_MODIFY)
        self.__manager.add_watch(str(CUR_DIR / 'parts' / 'floor2_children' / 'wall4_children'),
                                 pyinotify.IN_MODIFY)
        self.__manager.add_watch(str(CUR_DIR / 'parts' / 'floor2_children' / 'wall5_children'),
                                 pyinotify.IN_MODIFY)
        self.__manager.add_watch(str(CUR_DIR / 'parts' / 'floor2_children' / 'wall6_children'),
                                 pyinotify.IN_MODIFY)
