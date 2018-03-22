from blr.parts.mixins import Part

from .wall2_children import Diff0


class Wall2(Part):

    children = (
        Diff0,
    )
    name = 'Wall2'
    position = (
        6.,
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
