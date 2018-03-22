from blr.parts.mixins import Part


class Front1(Part):

    name = 'Front1'
    position = (
        0.,
        0.01,
        1.23
    )
    translate = (
        0.,
        0.,
        0.44,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0.,  0.,  0.],
                [0.,  .58, 0.],
                # ^
                [.65, .58, 0.],
                [.65, 0.,  0.],
            )
        return self._verts
