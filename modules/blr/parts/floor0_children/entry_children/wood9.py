from blr.parts.constants import WOOD_COLOR
from blr.parts.mixins import Part

from .wood9_children import Diff0


class Wood9(Part):

    children = (
        Diff0,
    )
    color = WOOD_COLOR
    name = 'Wood9'
    position = (
        -.35,
        1.,
        1.8,
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
                [0.,  1., 0.],
                # >
                [0.5, 1., 0.],
                [0.5, 0., 0.],
            )
        return self._verts
