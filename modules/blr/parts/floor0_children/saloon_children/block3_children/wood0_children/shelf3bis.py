from blr.parts.mixins import Part


class Shelf3bis(Part):

    name = 'Shelf3bis'
    position = (
        .02,
        .02,
        1.49,
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
                [0.,   .715, 0.],
                [0.,   0.96, 0.],
                # >
                [0.28, 0.96, 0.],
                [0.28, .715, 0.],
            )
        return self._verts
