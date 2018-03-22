from blr.parts.mixins import Part

from .canopy0_children import Diff0
from .canopy0_children import Diff1
from .canopy0_children import Diff2
from .canopy0_children import Diff3
from .canopy0_children import Diff4
from .canopy0_children import Diff5
from .canopy0_children import Diff6
from .canopy0_children import Diff7


class Canopy0(Part):

    children = (
        Diff0,
        Diff1,
        Diff2,
        Diff3,
        Diff4,
        Diff5,
        Diff6,
        Diff7,
    )
    color = (
        .0,
        .0,
        .0,
    )
    name = 'Canopy0'
    position = (
        3.8,
        3.,
        1.,
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
                # .
                [0.,   0.02, 0.],
                [0.,   0.08, 0.],
                # >
                [1.32, 0.08, 0.],
                [1.32, 1.58, 0.],
                # >
                [2.2,  1.58, 0.],
                [2.2,  1.52, 0.],
                # <
                [1.38, 1.52, 0.],
                [1.38, 0.02, 0.],
            )
        return self._verts
