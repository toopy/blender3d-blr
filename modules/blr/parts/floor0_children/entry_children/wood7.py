from blr.parts.constants import WOOD_COLOR
from blr.parts.mixins import Part

from .wood7_children import Diff0


class Wood7(Part):

    children = (
        Diff0,
    )
    color = WOOD_COLOR
    name = 'Wood7'
    position = (
        -.4,
        .5,
        1.4,
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
                [0.,   0.,  0.],
                [0.,   0.5, 0.],
                # >
                [0.5,  0.5, 0.],
                [0.5,  0.,  0.],
            )
        return self._verts
