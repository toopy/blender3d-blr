from blr.parts.mixins import Part


class Wall3(Part):

    name = 'Wall3'
    position = (
        1.4,
        0.,
        0.,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0.,  0., 0.],
                [0.,  0., 3.],
                # ^
                [1.6, 0., 3.],
                [1.6, 0., 0.],
            )
        return self._verts
