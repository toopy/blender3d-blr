from blr.parts.mixins import Part


class Door0(Part):

    name = 'Door0'
    position = (
        -.02,
        .005,
        .355,
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
