from blr.parts.mixins import Part


class Step1(Part):

    name = 'Step1'
    position = (
        0.,
        0.,
        0.4,
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
