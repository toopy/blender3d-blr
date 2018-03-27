from blr.parts.constants import WOOD_COLOR
from blr.parts.mixins import Part

from .wood0_children import Diff0
# from .wood0_children import Door0
# from .wood0_children import Door1
# from .wood0_children import Door2
# from .wood0_children import Door3
from .wood0_children import Shelf0
from .wood0_children import Shelf1
from .wood0_children import Shelf2
from .wood0_children import Shelf3
from .wood0_children import Shelf3bis
from .wood0_children import Shelf4
from .wood0_children import Shelf5
from .wood0_children import Shelf6
from .wood0_children import Shelf7
from .wood0_children import Shelf8
from .wood0_children import Shelf9
from .wood0_children import Shelf10
from .wood0_children import Shelf11
from .wood0_children import Shelf12
from .wood0_children import Shelf13
from .wood0_children import Shelf14
from .wood0_children import Shelf15
from .wood0_children import Shelf16
from .wood0_children import Shelf17
from .wood0_children import Shelf18
from .wood0_children import Shelf19
from .wood0_children import Shelf20
from .wood0_children import Shelf21
from .wood0_children import Shelf22
from .wood0_children import Shelf23
from .wood0_children import Shelf24
from .wood0_children import Shelf25
from .wood0_children import Shelf26
from .wood0_children import Shelf27
from .wood0_children import Shelf28
from .wood0_children import Shelf29
from .wood0_children import Shelf30


class Wood0(Part):

    children = (
        Diff0,
        # Door0,
        # Door1,
        # Door2,
        # Door3,
        Shelf0,
        Shelf1,
        Shelf2,
        Shelf3,
        Shelf3bis,
        Shelf4,
        Shelf5,
        Shelf6,
        # Shelf7,
        Shelf8,
        Shelf9,
        Shelf10,
        Shelf11,
        # Shelf12,
        Shelf13,
        Shelf14,
        Shelf15,
        Shelf16,
        # Shelf17,
        Shelf18,
        Shelf19,
        # Shelf20,
        Shelf21,
        Shelf22,
        Shelf23,
        Shelf24,
        # Shelf25,
        # Shelf26,
        Shelf27,
        Shelf28,
        Shelf29,
        Shelf30,
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
