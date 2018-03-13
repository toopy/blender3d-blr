from ..mixins import Part


class Floor1(Part):

    color = (
        .9,
        .6,
        .0,
    )
    name = 'Floor1'
    position = (
        3.,
        2.2,
        0.
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0., 0.,  0.],
                [0., 4.,  0.],
                # >
                [0.05, 4.,  0.],
                [0.05, 5.8,  0.],
                # >
                [3., 5.8, 0.],
                [3., 2.3, 0.],
                # <
                [2.2, 2.3, 0.],
                [2.2, .8, 0.],
                # <
                [1.2, .8, 0.],
                [1.2, .0, 0.],
            )
        return self._verts
