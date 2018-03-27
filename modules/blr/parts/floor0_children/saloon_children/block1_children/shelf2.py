from blr.parts.mixins import Part


class Shelf2(Part):

    name = 'Shelf2'
    position = (
        -.03,
        0.,
        1.75,
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
                [0., 0.,  0.],
                [0., 1.49, 0.],
                # >
                [.28, 1.49, 0.],
                [.28, 0.,  0.],
            )
        return self._verts
