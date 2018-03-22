from blr.parts.constants import WOOD_COLOR
from blr.parts.mixins import Part

from .block2_children import Door0
from .block2_children import Door1
from .block2_children import Shelf0
from .block2_children import Shelf1
from .block2_children import Shelf2
from .block2_children import Shelf3
from .block2_children import Shelf4


class Block2(Part):

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
    name = 'Block2'
    position = (
        2.67,
        0.,
        1.35,
    )
