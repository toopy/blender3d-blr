from ...constants import WOOD_COLOR
from ...mixins import Part


class Wood1(Part):

    color = WOOD_COLOR
    name = 'Wood1'
    position = (
        2.4,
        2.,
        .85,
    )
    translate = (
        0.,
        0.,
        .05,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0., 0., 0.],
                [0., .7, 0.],
                # ^
                [.6, .7, 0.],
                [.6, 0., 0.],
            )
        return self._verts
