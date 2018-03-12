from ...mixins import Part


class Diff0(Part):

    is_diff = True
    name = 'Diff0'
    position = (
        2.6,
        2.02,
        0.02,
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
                [0., 1.56, 3.16],
                [0., 1.56, 0.],
            )
        return self._verts
