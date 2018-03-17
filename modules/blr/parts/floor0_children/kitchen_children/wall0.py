from ...mixins import Part


class Wall0(Part):

    name = 'Wall0'
    position = (
        -.05,
        .5,
        0.,
    )
    translate = (
        0.,
        0.,
        1.1,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0.,  0., 0.],
                [0.,  2., 0.],
                # >
                [0.1, 2., 0.],
                [0.1, 0., 0.],
            )
        return self._verts
