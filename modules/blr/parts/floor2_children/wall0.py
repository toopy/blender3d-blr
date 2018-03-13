from ..mixins import Part


class Wall0(Part):

    name = 'Wall0'
    translate = (
        -0.1,
        0.,
        0.,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                [0.,   0., 0.],
                [0.,   4., 2.8],
                [0.,   8., 0.],
            )
        return self._verts
