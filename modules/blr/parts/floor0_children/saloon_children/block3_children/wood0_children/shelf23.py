from blr.parts.mixins import Part


class Shelf23(Part):

    name = 'Shelf23'
    position = (
        .02,
        .49,
        1.8825,
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
