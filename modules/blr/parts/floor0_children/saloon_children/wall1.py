from blr.parts.constants import DEFAULT_COLOR
from blr.parts.mixins import Part


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
                [0., 3.2, 3.],
                [0., 0.,  3.],
            )
        return self._verts
