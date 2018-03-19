from ...constants import WOOD_COLOR
from ...mixins import Part


class Shelf18(Part):

    color = WOOD_COLOR
    name = 'Shelf18'
    position = (
        2.45,
        0.59,
        0.,
    )
    translate = (
        0.,
        0.,
        .85,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0.,  0.,  0.],
                [0.,  .02, 0.],
                # ^
                [.55, .02, 0.],
                [.55, 0.,  0.],
            )
        return self._verts
