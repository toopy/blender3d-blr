from blr.parts.mixins import Part

from .wood0_children import Diff0


class Wood0(Part):

    children = (
        Diff0,
    )
    name = 'Wood0'
    position = (
        0.,
        0.,
        .85,
    )
    translate = (
        0.,
        0.,
        .05,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0., 0., 0.],
                [0., 1.3, 0.],
                # ^
                [.6, 1.3, 0.],
                [.6, 0., 0.],
            )
        return self._verts
