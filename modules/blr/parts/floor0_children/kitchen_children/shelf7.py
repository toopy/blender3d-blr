from ...constants import WOOD_COLOR
from ...mixins import Part


class Shelf7(Part):

    color = WOOD_COLOR
    name = 'Shelf7'
    position = (
        2.67,
        2.12,
        2.75,
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
                [0., 0.,  0.],
                [0., .58, 0.],
                # ^
                [.33, .58, 0.],
                [.33, 0.,  0.],
            )
        return self._verts
