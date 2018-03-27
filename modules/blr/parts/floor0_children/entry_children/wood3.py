from blr.parts.constants import WOOD_COLOR
from blr.parts.mixins import Part

from .wood3_children import Diff0


class Wood3(Part):

    children = (
        Diff0,
    )
    color = WOOD_COLOR
    name = 'Wood3'
    position = (
        -.35,
        0.5,
        0.4,
    )
    translate = (
        0.,
        0.,
        1.,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0., 0.,  0.],
                [0., .5, 0.],
                # >
                [.5, .5, 0.],
                [.5, 0.,  0.],
            )
        return self._verts
