from ...constants import WOOD_COLOR
from ...mixins import Part


class Door2(Part):

    color = WOOD_COLOR
    name = 'Door2'
    position = (
        2.65,
        2.105,
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
                [0.,  .59, 0.],
                # ^
                [.02, .59, 0.],
                [.02, 0.,  0.],
            )
        return self._verts
