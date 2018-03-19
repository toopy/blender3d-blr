from ...constants import WOOD_COLOR
from ...mixins import Part


class Door4(Part):

    color = WOOD_COLOR
    name = 'Door4'
    position = (
        2.65,
        0.,
        2.055,
    )
    translate = (
        0.,
        0.,
        .35,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0.,  0.,  0.],
                [0.,  1.2, 0.],
                # ^
                [.02, 1.2, 0.],
                [.02, 0.,  0.],
            )
        return self._verts
