from ...constants import WOOD_COLOR
from ...mixins import Part


class Shelf14(Part):

    color = WOOD_COLOR
    name = 'Shelf14'
    position = (
        2.42,
        0.,
        .1,
    )
    translate = (
        0.,
        0.,
        .02,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0.,  0.,  0.],
                [0.,  .59, 0.],
                # ^
                [.58, .59, 0.],
                [.58, 0.,  0.],
            )
        return self._verts
