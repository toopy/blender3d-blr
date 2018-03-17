from ...constants import WOOD_COLOR
from ...mixins import Part

from .wood4_children import Diff0


class Wood4(Part):

    children = (
        Diff0,
    )
    color = WOOD_COLOR
    name = 'Wood4'
    position = (
        -.4,
        1.,
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
                [0.,   0., 0.],
                [0.,   .5, 0.],
                # >
                [0.5,  .5, 0.],
                [0.5,  0., 0.],
            )
        return self._verts
