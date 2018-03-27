from blr.parts.mixins import Part


class Door3(Part):

    name = 'Door3'
    position = (
        .3,
        .0,
        2.4025,
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
                [0., 1., .595],
                [0., 0., .595],
            )
        return self._verts
