from blr.parts.mixins import Part


class Door0(Part):

    name = 'Door0'
    position = (
        -.05,
        0.,
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
                [0., 0.,     0.],
                [0., 0.,     .3575],
                # >
                [0., 1.4975, .3575],
                [0., 1.4975, 0.],
            )
        return self._verts
