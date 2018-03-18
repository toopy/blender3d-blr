from ...constants import WOOD_COLOR
from ...mixins import Part


class Wood4(Part):

    color = WOOD_COLOR
    name = 'Wood4'
    position = (
        2.45,
        0.,
        .45,
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
                [0.,  0.,  0.],
                [0.,  1.2, 0.],
                # ^
                [.55, 1.2, 0.],
                [.55, 0.,  0.],
            )
        return self._verts
