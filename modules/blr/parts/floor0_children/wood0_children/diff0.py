from ...mixins import Part


class Diff0(Part):

    is_diff = True
    name = 'Diff0'
    position = (
        -.1,
        .02,
        .02,
    )
    translate = (
        0.8,
        0.,
        0.,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0., 0.,  0.],
                [0., 0.,  3.16],
                # >
                [0., 1.46, 3.16],
                [0., 1.46, 0.],
            )
        return self._verts
