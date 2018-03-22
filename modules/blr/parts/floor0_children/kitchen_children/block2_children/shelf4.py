from blr.parts.mixins import Part


class Shelf4(Part):

    name = 'Shelf4'
    position = (
        0.,
        1.18,
        .35,
    )
    translate = (
        0.,
        .02,
        0.,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0., 0.,  0.],
                [0., 0., .72],
                # ^
                [.33, 0., .72],
                [.33, 0., 0.],
            )
        return self._verts
