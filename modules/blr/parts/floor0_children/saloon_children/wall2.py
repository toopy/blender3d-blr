from ...mixins import Part
from ...mixins import DEFAULT_COLOR


class Wall2(Part):

    color = DEFAULT_COLOR
    name = 'Wall2'
    position = (
        2.95,
        0.,
        0.,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0., 0., 0.],
                [0., 2., 0.],
                # ^
                [0., 2., 3.],
                [0., 0., 3.],
            )
        return self._verts
