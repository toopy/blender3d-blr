from ...mixins import Part


class Wall3(Part):

    name = 'Wall3'
    position = (
        2.4,
        2.,
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
