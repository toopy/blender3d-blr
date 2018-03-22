from blr.parts.constants import DEFAULT_COLOR
from blr.parts.mixins import Part


class Wall0(Part):

    color = DEFAULT_COLOR
    name = 'Wall0'
    position = (
        0.,
        1.2,
        0.,
    )
    translate = (
        0.,
        0.,
        .85,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0.,  0., 0.],
                [0.,  .1, 0.],
                # ^
                [.6, .1, 0.],
                [.6, 0., 0.],
            )
        return self._verts
