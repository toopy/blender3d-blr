from blr.parts.mixins import Part


class Door1(Part):

    name = 'Door1'
    position = (
        -.05,
        0.,
        2.1125,
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
