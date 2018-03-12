from ...mixins import Part


class Wall0(Part):

    color = (
        .8,
        .8,
        .0,
    )
    name = 'Wall0'
    position = (
        0.,
        3.2,
        0.,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0., 0.,  0.],
                [0., 1.6, 0.],
                # ^
                [0., 1.6, 3.2],
                [0., 0.,  3.2],
            )
        return self._verts
