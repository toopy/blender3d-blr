from ...constants import WOOD_COLOR
from ...mixins import Part

from .wood2_children import Diff0


class Wood2(Part):

    children = (
        Diff0,
    )
    color = WOOD_COLOR
    name = 'Wood2'
    position = (
        -.4,
        0.,
        0.4,
    )
    translate = (
        0.,
        0.,
        1.4,
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
