from ...constants import WOOD_COLOR
from ...mixins import Part


class Shelf13(Part):

    color = WOOD_COLOR
    name = 'Shelf13'
    position = (
        2.67,
        1.18,
        2.05,
    )
    translate = (
        0.,
        .02,
        0.,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0., 0.,  0.],
                [0., 0., .72],
                # ^
                [.33, 0., .72],
                [.33, 0., 0.],
            )
        return self._verts
