from blr.parts.mixins import Part

from .wall6_children import Diff0


class Wall6(Part):

    children = (
        Diff0,
    )
    name = 'Wall6'
    translate = (
        0.,
        0.,
        2.9,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [2.55, 3.,   0.],
                [2.55, 6.75, 0.],
                # >
                [2.65, 6.75, 0.],
                [2.65, 3.1,  0.],
                # >
                [2.95, 3.1,  0.],
                [2.95, 3.,   0.],
            )
        return self._verts
