from blr.parts.mixins import Part


class Door1(Part):

    name = 'Door1'
    position = (
        -.02,
        .005,
        .715,
    )
    translate = (
        0.,
        0.,
        .35,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0.,  0.,  0.],
                [0.,  .59, 0.],
                # ^
                [.02, .59, 0.],
                [.02, 0.,  0.],
            )
        return self._verts
