from blr.parts.mixins import Part


class Shelf4(Part):

    name = 'Shelf4'
    position = (
        -.03,
        .01,
        1.4,
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
                [0.,  .47, 0.],
                # >
                [.28, .47, 0.],
                [.28, 0.,  0.],
            )
        return self._verts
