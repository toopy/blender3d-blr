from ..mixins import Part


class Kitchen(Part):

    name = 'Kitchen'
    position = (
        3.,
        4.55,
        0.,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0.,  3.45, 0.],
                # >
                [3.,  3.45, 0.],
                [3.,  0,    0.],
                # <
                [1.5, 0,    0.],
                [1.5, .5,   0.],
                # <
                [1.,  .5,   0.],
                [1.,  .45,  0.],
                # <
                [.2,  .45,  0.],
                [.2,  .5,   0.],
                # <
                [.05, .5,   0.],
                [.05, 2.65, 0.],
                # <
                [0.,  2.65, 0.],
            )
        return self._verts
