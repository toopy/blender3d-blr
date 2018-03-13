from ...mixins import Part


class Diff5(Part):

    is_diff = True
    name = 'Diff5'
    position = (
        1.3,
        1.,
        0.,
    )
    translate = (
        .1,
        0.,
        0.,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0.,  0.06, 0.06],
                [0.,  0.06, 0.94],
                # >
                [0., 0.48, 0.94],
                [0., 0.48, 0.06],
            )
        return self._verts
