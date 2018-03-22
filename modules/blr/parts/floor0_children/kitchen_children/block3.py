from blr.parts.constants import WOOD_COLOR
from blr.parts.mixins import Part

from .block3_children import Door0
from .block3_children import Shelf0
from .block3_children import Shelf1
from .block3_children import Wall0
from .block3_children import Wood0


class Block3(Part):

    children = (
        Door0,
        Shelf0,
        Shelf1,
        Wall0,
        Wood0,
    )
    color = WOOD_COLOR
    name = 'Block3'
    position = (
        2.4,
        2.,
        0.,
    )
