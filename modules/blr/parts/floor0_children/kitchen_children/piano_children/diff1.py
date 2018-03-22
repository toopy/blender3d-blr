from blr.parts.mixins import Part


class Diff1(Part):

    is_diff = True
    name = 'Diff1'
    position = (
        .01,
        .01,
        .79,
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
                [0.,   0.,  0.],
                [0.,   .68, 0.],
                # >
                [0.57, .68, 0.],
                [0.57, 0.,  0.],
            )
        return self._verts
