import logging

import bpy
import bmesh

from .utils import Watcher
from .parts import Floor0
from .parts import Floor2

logger = logging.getLogger(__name__)


def build(context, operator='blr_floor0'):

    logger.info('build: %s', operator)

    if operator.endswith('blr_all') or operator.endswith('blr_floor0'):
        Floor0(context).build()

    if operator.endswith('blr_all') or operator.endswith('blr_floor2'):
        Floor2(context).build()


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
