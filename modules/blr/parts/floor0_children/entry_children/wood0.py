from blr.parts.constants import WOOD_COLOR
from blr.parts.mixins import Part

from .wood0_children import Diff0


class Wood0(Part):

    children = (
        Diff0,
    )
    color = WOOD_COLOR
    name = 'Wood0'
    position = (
        -.35,
        0.,
        0.,
    )
    translate = (
        0.,
        0.,
        .4,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0.,  0., 0.],
                [0.,  .5, 0.],
                # >
                [0.5, .5, 0.],
                [0.5, 0., 0.],
            )
        return self._verts
