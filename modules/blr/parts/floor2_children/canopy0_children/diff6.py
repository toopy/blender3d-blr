from blr.parts.mixins import Part


class Diff6(Part):

    is_diff = True
    name = 'Diff6'
    position = (
        1.38,
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
