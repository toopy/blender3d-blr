from ..mixins import Part


class Wall7(Part):

    name = 'Wall7'
    position = (
        3.8,
        3.,
        0.,
    )
    translate = (
        0.,
        0.,
        1.,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                [0.,  0.,  0.],
                [0.,  0.1, 0.],
                [1.3, 0.1, 0.],
                [1.3, 1.6, 0.],
                [2.2, 1.6, 0.],
                [2.2, 1.5, 0.],
                [1.4, 1.5, 0.],
                [1.4, 0.,  0.],
            )
        return self._verts
