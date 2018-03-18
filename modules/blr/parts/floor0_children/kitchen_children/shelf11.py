from ...constants import WOOD_COLOR
from ...mixins import Part


class Shelf11(Part):

    color = WOOD_COLOR
    name = 'Shelf11'
    position = (
        2.67,
        0.,
        2.4,
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
                [0.,  0.,   0.],
                [0.,  1.18, 0.],
                # ^
                [.33, 1.18, 0.],
                [.33, 0.,   0.],
            )
        return self._verts
