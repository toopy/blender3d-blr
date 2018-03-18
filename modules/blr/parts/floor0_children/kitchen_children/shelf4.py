from ...constants import WOOD_COLOR
from ...mixins import Part


class Shelf4(Part):

    color = WOOD_COLOR
    name = 'Shelf4'
    position = (
        2.67,
        2.1,
        1.7,
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
                [0., 0., 0.],
                [0., .6, 0.],
                # ^
                [.33, .6, 0.],
                [.33, 0., 0.],
            )
        return self._verts
