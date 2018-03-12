from ..mixins import Part

from .wood0_children import Diff0


class Wood0(Part):

    children = (
        Diff0,
    )
    color = (
        .9,
        .6,
        .0,
    )
    name = 'Wood0'
    position = (
        2.7,
        2.,
        0.,
    )
    translate = (
        0.6,
        0.,
        0.,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0., 0.,  0.],
                [0., 0.,  3.2],
                # >
                [0., 1.6, 3.2],
                [0., 1.6, 0.],
            )
        return self._verts
