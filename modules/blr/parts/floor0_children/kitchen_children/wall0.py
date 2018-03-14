from ...mixins import Part


class Wall0(Part):

    name = 'Wall0'
    translate = (
        0.,
        0.,
        1.,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0.,   0.,   0.],
                [0.,   2.5,  0.],
                # >
                [0.1,  2.5,  0.],
                [0.1,  0.,   0.],
            )
        return self._verts
