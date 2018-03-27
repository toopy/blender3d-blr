from blr.parts.mixins import Part


class Door1(Part):

    name = 'Door1'
    position = (
        -.05,
        .0025,
        1.75,
    )
    translate = (
        .02,
        0.,
        0.,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0., 0., 0.],
                [0., 0., .72],
                # >
                [0., .495, .72],
                [0., .495, 0.],
            )
        return self._verts
