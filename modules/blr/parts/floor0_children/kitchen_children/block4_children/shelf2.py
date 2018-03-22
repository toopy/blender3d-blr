from blr.parts.mixins import Part


class Shelf2(Part):

    name = 'Shelf2'
    position = (
        .02,
        0.58,
        0.,
    )
    translate = (
        0.,
        0.,
        .85,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0.,  0.,  0.],
                [0.,  .02, 0.],
                # ^
                [.55, .02, 0.],
                [.55, 0.,  0.],
            )
        return self._verts
