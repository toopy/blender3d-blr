from blr.parts.mixins import Part


class Floor0(Part):

    color = (
        .9,
        .6,
        .0,
    )
    name = 'Floor0'

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0.,   0.,  0.],
                [0.,   8.,  0.],
                # <
                [2.95, 8.,  0.],
                [2.95, 6.2, 0.],
                # >
                [3.,   6.2, 0.],
                [3.,   2.2, 0.],
                # <
                [2.95, 2.2, 0.],
                [2.95, 0.,  0.],
            )
        return self._verts
