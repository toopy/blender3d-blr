from ..mixins import Part


class Kitchen(Part):

    name = 'Kitchen'
    position = (
        3.,
        4.5,
        0.,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0.,  3.5, 0.],
                # >
                [3.,  3.5, 0.],
                [3.,  0,    0.],
                # <
                [1.5, 0,    0.],
                [1.5, .55,   0.],
                # <
                [1.,  .55,   0.],
                [1.,  .45,  0.],
                # <
                [.2,  .45,  0.],
                [.2,  .55,   0.],
                # <
                [.05, .55,   0.],
                [.05, 2.65, 0.],
                # <
                [0.,  2.65, 0.],
            )
        return self._verts
