from blr.parts.constants import WOOD_COLOR
from blr.parts.mixins import Part


class Wood0(Part):

    color = WOOD_COLOR
    name = 'Wood0'
    position = (
        0.,
        0.,
        0.8,
    )
    translate = (
        0.,
        0.,
        .12,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0.,   0.,  0.],
                [0.,   1.2, 0.],
                # >
                [0.65, 1.2, 0.],
                [0.65, 0.,  0.],
            )
        return self._verts
