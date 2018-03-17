from ...constants import DEFAULT_COLOR
from ...mixins import Part


class Wall0(Part):

    color = DEFAULT_COLOR
    name = 'Wall0'

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0., 0.,  0.],
                [0., 3.2, 0.],
                # ^
                [0., 3.2, 3.],
                [0., 0.,  3.],
            )
        return self._verts
