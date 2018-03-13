from ..mixins import Part

from .wall3_children import Diff0


class Wall3(Part):

    children = (
        Diff0,
    )
    name = 'Wall3'
    translate = (
        0.,
        -0.2,
        0.,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0.,   1.25, 0.],
                [0.,   1.25, 1.5],
                # .
                [2.95, 1.25, 1.5],
                [2.95, 1.25, 0.],
            )
        return self._verts
