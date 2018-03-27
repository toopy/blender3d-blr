from blr.parts.mixins import Part


class Door0(Part):

    name = 'Door0'
    position = (
        .3,
        .0,
        0.0025,
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
                [0., 1., 0.],
                # >
                [0., 1., .795],
                [0., 0., .795],
            )
        return self._verts
