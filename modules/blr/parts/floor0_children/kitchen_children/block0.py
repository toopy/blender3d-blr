from blr.parts.constants import WOOD_COLOR
from blr.parts.mixins import Part

from .block0_children import Door0
from .block0_children import Door1
from .block0_children import Shelf0
from .block0_children import Shelf1
from .block0_children import Shelf2
from .block0_children import Shelf3


class Block0(Part):

    children = (
        Door0,
        Door1,
        Shelf0,
        Shelf1,
        Shelf2,
        Shelf3,
    )
    color = WOOD_COLOR
    name = 'Block0'
    position = (
        2.42,
        2.8,
        1.7,
    )
