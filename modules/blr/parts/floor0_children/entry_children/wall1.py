from ...mixins import Part


class Wall1(Part):

    color = (
        .8,
        .8,
        .8,
    )
    name = 'Wall1'
    position = (
        3.,
        3.1,
        0.
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0.,  0., 0.],
                [0.,  0., 3.2],
                # >
                [.05, 0., 3.2],
                [.05, 0., 0.],
            )
        return self._verts
