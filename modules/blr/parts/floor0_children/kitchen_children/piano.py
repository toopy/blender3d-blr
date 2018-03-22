from blr.parts.mixins import Part

from .piano_children import Back
from .piano_children import Diff0
from .piano_children import Diff1


class Piano(Part):

    children = (
        Back,
        Diff0,
        Diff1,
    )
    color = (
        1.,
        1.,
        1.,
    )
    name = 'Piano'
    position = (
        2.4,
        1.3,
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
