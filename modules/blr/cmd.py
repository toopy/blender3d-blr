import logging

import bpy

from .utils import Watcher
from .parts import Floor0
from .parts import Floor2

logger = logging.getLogger(__name__)


def build(context, operator='blr_floor0'):

    logger.info('build: %s', operator)

    floor0 = Floor0(context)
    floor2 = Floor2(context)

    if operator.endswith('blr_all'):
        floor0.build()
        floor2.position = (0., 0., 6.4)
        floor2.build()
    elif operator.endswith('blr_floor0'):
        floor0.build()
    elif operator.endswith('blr_floor2'):
        floor2.build()


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


def rebuild(context, operator='blr_floor0'):
    clean(context)
    build(context, operator=operator)


def run(context, operator):
    rebuild(context, operator=operator.bl_idname)
    Watcher().watch(context, operator=operator.bl_idname)


__all__ = (
    'build',
    'clean',
    'run',
)
