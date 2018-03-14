from ...mixins import Part


class Wall1(Part):

    name = 'Wall1'
    position = (
        1.9,
        3.4,
        0.,
    )
    translate = (
        0.,
        0.,
        3.,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0.1,  0., 0.],
                [0.,  .1, 0.],
                # ^
                [1.1, .1, 0.],
                [1.1,  0., 0.],
            )
        return self._verts
