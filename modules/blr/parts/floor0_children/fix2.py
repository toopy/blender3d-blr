from blr.parts.mixins import Part


class Fix2(Part):

    color = (
        .8,
        .8,
        .0,
    )
    name = 'Fix2'
    position = (
        2.95,
        2.,
        0.,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0.,  0.,  0.],
                [0.,  1.1, 0.],
                # >
                [0.1, 1.1, 0.],
                [0.1, 0.,  0.],
            )
        return self._verts
