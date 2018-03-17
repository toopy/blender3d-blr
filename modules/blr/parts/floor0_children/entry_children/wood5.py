from ...constants import WOOD_COLOR
from ...mixins import Part

from .wood5_children import Diff0


class Wood5(Part):

    children = (
        Diff0,
    )
    color = WOOD_COLOR
    name = 'Wood5'
    position = (
        -.4,
        1.5,
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
