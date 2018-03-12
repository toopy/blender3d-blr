from ...mixins import Part


class Floor(Part):

    color = (
        .8,
        .8,
        .0,
    )
    name = 'Floor'
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
                [0., .0,  0.],
                [.8, .8,  0.],
                [0., 1.6, 0.],
            )
        return self._verts
