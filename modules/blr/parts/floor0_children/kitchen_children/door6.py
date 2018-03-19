from ...constants import WOOD_COLOR
from ...mixins import Part


class Door6(Part):

    color = WOOD_COLOR
    name = 'Door6'
    position = (
        2.4,
        0.0025,
        .1,
    )
    translate = (
        0.,
        0.,
        .75,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0.,  0.,  0.],
                [0.,  .595, 0.],
                # ^
                [.02, 0.595, 0.],
                [.02, 0.,  0.],
            )
        return self._verts
