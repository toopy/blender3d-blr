from ...constants import WOOD_COLOR
from ...mixins import Part


class Door0(Part):

    color = WOOD_COLOR
    name = 'Door0'
    position = (
        2.3,
        2.805,
        2.175,
    )
    translate = (
        0.,
        0.,
        .41,
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
