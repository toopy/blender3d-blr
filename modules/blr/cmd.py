import logging

import bpy
import bmesh

from .utils import Watcher
from .parts import Floor0

logger = logging.getLogger(__name__)


def build(context):

    logger.info('build')

    Floor0(context).build()

    # for obj in bpy.data.objects:
    #     obj.select = True
    # bpy.ops.view3d.localview()


def clean(context):

    logger.info('clean')

    # deselect all
    bpy.ops.object.select_all(action='DESELECT')

    # select and delete one by one
    for obj in bpy.context.scene.objects:
        # select
        obj.select = True
        # delect
        bpy.ops.object.delete()


def rebuild(context):
    clean(context)
    build(context)


def run(context):
    rebuild(context)
    Watcher().watch(context)


__all__ = (
    'build',
    'clean',
    'run',
)
