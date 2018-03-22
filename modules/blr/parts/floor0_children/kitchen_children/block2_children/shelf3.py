from blr.parts.mixins import Part


class Shelf3(Part):

    name = 'Shelf3'
    position = (
        0.,
        0.,
        1.05,
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
                [0., 0.,   0.],
                [0., 1.18, 0.],
                # ^
                [.33, 1.18, 0.],
                [.33, 0.,   0.],
            )
        return self._verts
