from blr.parts.mixins import Part


class Step0(Part):

    name = 'Step0'
    position = (
        0.,
        0.,
        0.15,
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
                [0.,   0.,   0.],
                [0.,   1.16, 0.],
                # >
                [0.61, 1.16, 0.],
                [0.61, 0.,   0.],
            )
        return self._verts
