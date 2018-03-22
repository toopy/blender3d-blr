from blr.parts.mixins import Part

from .wall5_children import Diff0


class Wall5(Part):

    children = (
        Diff0,
    )
    name = 'Wall5'
    position = (
        3.05,
        4.,
        0.,
    )
    translate = (
        0.,
        0.,
        1.5,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0.,   2.75,  0.],
                [0.,   2.95,  0.],
                # >
                [2.95, 2.95,  0.],
                [2.95, 2.75,  0.],
            )
        return self._verts
