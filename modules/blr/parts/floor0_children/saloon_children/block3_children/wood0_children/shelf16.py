from blr.parts.mixins import Part


class Shelf16(Part):

    name = 'Shelf16'
    position = (
        .02,
        .245,
        1.1375,
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
                [0.,   0., 0.],
                [0.,   0., .36],
                # >
                [0.28, 0., .36],
                [0.28, 0., 0.],
            )
        return self._verts
