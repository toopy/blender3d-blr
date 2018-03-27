from blr.parts.mixins import Part


class Shelf12(Part):

    name = 'Shelf12'
    position = (
        .02,
        .735,
        .3925,
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
