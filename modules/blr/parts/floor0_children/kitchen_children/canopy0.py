from blr.parts.mixins import Part

from .canopy0_children import Diff0
from .canopy0_children import Diff1
from .canopy0_children import Diff2
from .canopy0_children import Diff3


class Canopy0(Part):

    children = (
        Diff0,
        Diff1,
        Diff2,
        Diff3,
    )
    color = (
        .0,
        .0,
        .0,
    )
    name = 'Canopy0'
    position = (
        -0.03,
        0.5,
        1.1,
    )
    translate = (
        0.,
        0.,
        1.9,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0.,   0.,  0.],
                [0.,   2.,  0.],
                # >
                [0.06, 2.,  0.],
                [0.06, 0.,  0.],
            )
        return self._verts
