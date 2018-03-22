from blr.parts.mixins import Part


class Diff0(Part):

    is_diff = True
    name = 'Diff0'
    position = (
        -.05,
        .02,
        .02,
    )
    translate = (
        .6,
        0.,
        0.,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0.,  0.,  0.],
                [0.,  .96, 0.],
                # >
                [0.,  .96, 0.36],
                [0.,  0.,  0.36],
            )
        return self._verts
