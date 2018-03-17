from ...constants import WOOD_COLOR
from ...mixins import Part

from .wood0_children import Diff0


class Wood0(Part):

    children = (
        Diff0,
    )
    color = WOOD_COLOR
    name = 'Wood0'
    position = (
        .05,
        .5,
        0.,
    )
    translate = (
        0.,
        0.,
        .9,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0.,  0., 0.],
                [0.,  2., 0.],
                # >
                [0.5, 2., 0.],
                [0.5, 0., 0.],
            )
        return self._verts
