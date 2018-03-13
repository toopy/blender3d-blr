from ...mixins import Part


class Diff7(Part):

    is_diff = True
    name = 'Diff7'
    position = (
        1.76,
        1.5,
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
                [.08, 0., 0.06],
                [.08, 0., 0.94],
                # >
                [.4,  0., 0.94],
                [.4,  0., 0.06],
            )
        return self._verts
