from blr.parts.mixins import Part


class Shelf26(Part):

    name = 'Shelf26'
    position = (
        .02,
        .49,
        2.255,
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
