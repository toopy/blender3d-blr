from ...constants import WOOD_COLOR
from ...mixins import Part


class Door5(Part):

    color = WOOD_COLOR
    name = 'Door5'
    position = (
        2.65,
        0.,
        2.415,
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
