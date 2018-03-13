from ...mixins import Part


class Diff1(Part):

    is_diff = True
    name = 'Diff1'
    position = (
        0.42,
        0.,
        0.,
    )
    translate = (
        0.,
        .1,
        0.,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [.06,  0., 0.06],
                [.06,  0., 0.94],
                # >
                [.42, 0., 0.94],
                [.42, 0., 0.06],
            )
        return self._verts
