from blr.parts.mixins import Part

from .wall8_children import Diff0


class Wall8(Part):

    children = (
        Diff0,
    )
    name = 'Wall8'
    position = (
        3.8,
        3.,
        2.,
    )
    translate = (
        0.,
        0.,
        1.,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                [0.,  0.,  0.],
                [0.,  0.1, 0.],
                [1.3, 0.1, 0.],
                [1.3, 1.6, 0.],
                [2.2, 1.6, 0.],
                [2.2, 1.5, 0.],
                [1.4, 1.5, 0.],
                [1.4, 0.,  0.],
            )
        return self._verts
