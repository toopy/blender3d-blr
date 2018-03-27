from blr.parts.constants import WOOD_COLOR
from blr.parts.mixins import Part

from .block1_children import Door0
from .block1_children import Door1
from .block1_children import Shelf0
from .block1_children import Shelf1
from .block1_children import Shelf2
from .block1_children import Shelf3
from .block1_children import Shelf4


class Block1(Part):

    children = (
        Door0,
        Door1,
        Shelf0,
        Shelf1,
        Shelf2,
        Shelf3,
        Shelf4,
    )
    color = WOOD_COLOR
    name = 'Block1'
    position = (
        2.7,
        0.,
        0.,
    )
