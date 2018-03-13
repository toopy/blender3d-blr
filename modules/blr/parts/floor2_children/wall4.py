from ..mixins import Part

from .wall4_children import Diff0


class Wall4(Part):

    children = (
        Diff0,
    )
    name = 'Wall4'
    position = (
        0.,
        4.,
        0.,
    )
    translate = (
        0.,
        0.2,
        0.,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0.,   2.75, 0.],
                [0.,   2.75, 1.5],
                # .
                [2.95, 2.75, 1.5],
                [2.95, 2.75, 0.],
            )
        return self._verts
