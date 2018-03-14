from ..mixins import Part

from .wood0_children import Beam0
from .wood0_children import Beam1
from .wood0_children import Shelf0
from .wood0_children import Shelf1
from .wood0_children import Shelf2
from .wood0_children import Shelf3
from .wood0_children import Shelf4


class Wood0(Part):

    children = (
        Beam0,
        Beam1,
        Shelf0,
        Shelf1,
        Shelf2,
        Shelf3,
        Shelf4,
    )
    color = (
        .9,
        .6,
        .0,
    )
    name = 'Wood0'
    position = (
        2.8,
        2.,
        0.,
    )
