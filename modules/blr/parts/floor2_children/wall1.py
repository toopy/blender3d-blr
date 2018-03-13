from ..mixins import Part
from .wall1_children import Diff0


class Wall1(Part):

    children = (
        Diff0,
    )
    name = 'Wall1'
    position = (
        2.95,
        0.,
        0.
    )
    translate = (
        0.1,
        0.,
        0.,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                [0., 0., 0.],
                [0., 4., 2.8],
                [0., 8., 0.],
            )
        return self._verts
