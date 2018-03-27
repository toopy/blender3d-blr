from blr.parts.constants import WOOD_COLOR
from blr.parts.mixins import Part

from .block0_children import Door0
from .block0_children import Door1
from .block0_children import Shelf0
from .block0_children import Shelf1
from .block0_children import Shelf2
from .block0_children import Shelf3
from .block0_children import Shelf4
from .block0_children import Shelf5
from .block0_children import Shelf6
from .block0_children import Wood0
from .block0_children import Wood1


class Block0(Part):

    children = (
        Door0,
        Door1,
        Shelf0,
        Shelf1,
        Shelf2,
        Shelf3,
        Shelf4,
        Shelf5,
        Shelf6,
        Wood0,
        Wood1,
    )
    color = WOOD_COLOR
    name = 'Block0'
    position = (
        2.7,
        1.5,
        0.,
    )
