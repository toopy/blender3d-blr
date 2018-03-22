from blr.parts.mixins import Part


class Shelf2(Part):

    name = 'Shelf2'
    position = (
        0.,
        0.,
        .7,
    )
    translate = (
        0.,
        0.,
        .02,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0.,  0.,  0.],
                [0.,  .58, 0.],
                # ^
                [.33, .58, 0.],
                [.33, 0.,  0.],
            )
        return self._verts
