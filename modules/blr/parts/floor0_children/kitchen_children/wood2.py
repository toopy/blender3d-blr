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
        2.4,
        0.,
        .85,
    )
    translate = (
        0.,
        0.,
        .05,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0., 0., 0.],
                [0., 1.3, 0.],
                # ^
                [.6, 1.3, 0.],
                [.6, 0., 0.],
            )
        return self._verts
