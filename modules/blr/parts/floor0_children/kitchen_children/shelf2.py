from ...constants import WOOD_COLOR
from ...mixins import Part


class Shelf2(Part):

    color = WOOD_COLOR
    name = 'Shelf2'
    position = (
        2.42,
        2.8,
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
                [0., 0., 0.],
                [0., .6, 0.],
                # ^
                [.58, .6, 0.],
                [.58, 0., 0.],
            )
        return self._verts
