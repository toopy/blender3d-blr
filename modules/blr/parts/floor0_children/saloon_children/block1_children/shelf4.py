from blr.parts.mixins import Part


class Shelf4(Part):

    name = 'Shelf4'
    position = (
        -.03,
        0.,
        2.45,
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
