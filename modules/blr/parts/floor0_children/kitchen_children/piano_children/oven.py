from ....mixins import Part

from .oven_children import Back
from .oven_children import Diff0
from .oven_children import Diff1


class Oven(Part):

    children = (
        Back,
        Diff0,
        Diff1,
    )
    name = 'Oven'
    position = (
        0.,
        0.,
        .1,
    )
    translate = (
        0.,
        0.,
        .8,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0,  0., 0.],
                [0,  .7, 0.],
                # >
                [.6, .7, 0.],
                [.6, 0., 0.],
            )
        return self._verts
