from ..mixins import Part


class Fix1(Part):

    color = (
        .8,
        .8,
        .0,
    )
    name = 'Fix1'
    position = (
        2.95,
        3.9,
        0.,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0.,   0.,   0.],
                [0.,   3.3,  0.],
                # >
                [0.1,  3.3,  0.],
                [0.1,  1.15, 0.],
                # >
                [0.25, 1.15, 0.],
                [0.25, 1.05, 0.],
                #
                [0.1,  1.05, 0.],
                [0.1,  0.,   0.],
            )
        return self._verts
