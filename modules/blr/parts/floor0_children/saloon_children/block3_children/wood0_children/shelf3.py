from blr.parts.mixins import Part


class Shelf3(Part):

    name = 'Shelf3'
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
                [0.,   0.,   0.],
                [0.,   0.245, 0.],
                # >
                [0.28, 0.245, 0.],
                [0.28, 0.,   0.],
            )
        return self._verts
