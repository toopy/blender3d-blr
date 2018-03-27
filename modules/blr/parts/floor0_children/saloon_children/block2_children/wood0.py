from blr.parts.constants import WOOD_COLOR
from blr.parts.mixins import Part

from .wood0_children import Diff0
from .wood0_children import Door0
from .wood0_children import Door1
from .wood0_children import Door2
from .wood0_children import Door3
from .wood0_children import Shelf0
from .wood0_children import Shelf1
from .wood0_children import Shelf2
from .wood0_children import Shelf3
from .wood0_children import Shelf4
from .wood0_children import Shelf5


class Wood0(Part):

    children = (
        Diff0,
        Door0,
        Door1,
        Door2,
        Door3,
        Shelf0,
        Shelf1,
        Shelf2,
        Shelf3,
        Shelf4,
        Shelf5,
    )
    color = WOOD_COLOR
    name = 'Wood0'
    position = (
        0.,
        0.,
        0.,
    )
    translate = (
        0.,
        0.,
        3.,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0., 0., 0.],
                [0., 1., 0.],
                # >
                [.3, 1., 0.],
                [.3, 0., 0.],
            )
        return self._verts
