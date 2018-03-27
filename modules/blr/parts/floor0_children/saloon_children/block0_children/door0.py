from blr.parts.mixins import Part


class Door0(Part):

    name = 'Door0'
    position = (
        -.05,
        .0025,
        0.,
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
