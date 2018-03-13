from ...mixins import Part
from ...mixins import DEFAULT_COLOR


class Wall1(Part):

    color = DEFAULT_COLOR
    name = 'Wall1'
    position = (
        0.,
        4.8,
        0.,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0., 0.,  0.],
                [0., 3.2, 0.],
                # ^
                [0., 3.2, 3.2],
                [0., 0.,  3.2],
            )
        return self._verts
