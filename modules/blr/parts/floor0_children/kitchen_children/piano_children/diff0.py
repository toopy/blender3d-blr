from blr.parts.mixins import Part


class Diff0(Part):

    is_diff = True
    name = 'Diff0'
    position = (
        -.01,
        .01,
        .10,
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
                [0.,  0.,  0.],
                [0.,  .68, 0.],
                # >
                [0.,  .68, 0.55],
                [0.,  0.,  0.55],
            )
        return self._verts
