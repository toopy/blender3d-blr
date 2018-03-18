from ...mixins import Part


class Wall4(Part):

    name = 'Wall4'
    position = (
        2.4,
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
