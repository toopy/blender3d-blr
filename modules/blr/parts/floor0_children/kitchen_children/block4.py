from blr.parts.constants import WOOD_COLOR
from blr.parts.mixins import Part

from .block4_children import Basin
from .block4_children import Door0
from .block4_children import Shelf0
from .block4_children import Shelf1
from .block4_children import Shelf2
from .block4_children import Wall0
from .block4_children import Wood0


class Block4(Part):

    children = (
        Basin,
        Door0,
        Shelf0,
        Shelf1,
        Shelf2,
        Wall0,
        Wood0,
    )
    color = WOOD_COLOR
    name = 'Block4'
    position = (
        2.4,
        0.,
        0.,
    )
