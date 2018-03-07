import logging

import bpy
import bmesh

from .floor0_children import Floor
from .mixins import Part

logger = logging.getLogger(__name__)


class Floor0(Part):

    children = (
        Floor,
    )
    name = 'Floor 0'
