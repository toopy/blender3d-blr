from blr.parts.mixins import Part


class Wood1(Part):

    name = 'Wood1'
    position = (
        -.03,
        .48,
        0.,
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
                [0.,  0., 0.],
                [0.,  0., 2.47],
                # >
                [.28, 0., 2.47],
                [.28, 0., 0.],
            )
        return self._verts
