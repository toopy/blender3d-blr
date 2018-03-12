from ...mixins import Part


class Wall2(Part):

    color = (
        .8,
        .8,
        .8,
    )
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
                [0., 0.,  0.],
                [0., 0.,  3.2],
                # ^
                [0., 2., 3.2],
                [0., 2., 0.],
            )
        return self._verts
