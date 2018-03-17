from ...constants import WOOD_COLOR
from ...mixins import Part


class Shelf2(Part):

    color = WOOD_COLOR
    name = 'Shelf2'
    position = (
        2.32,
        2.8,
        2.17,
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
                [.68, .6, 0.],
                [.68, 0., 0.],
            )
        return self._verts
