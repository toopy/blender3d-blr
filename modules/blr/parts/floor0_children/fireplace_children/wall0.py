from ...mixins import Part


class Wall0(Part):

    name = 'Wall0'

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0., 0.,  0.],
                [0., 1.6, 0.],
                # ^
                [0., 1.6, 3.],
                [0., 0.,  3.],
            )
        return self._verts
