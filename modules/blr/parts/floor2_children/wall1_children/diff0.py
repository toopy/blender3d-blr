from blr.parts.mixins import Part


class Diff0(Part):

    is_diff = True
    name = 'Diff0'
    position = (
        -.1,
        .0,
        -.2,
    )
    translate = (
        0.3,
        0.,
        0.,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0., 2.2, 0.],
                [0., 2.2, 2.2],
                # >
                [0., 6.2, 2.2],
                [0., 6.2, 0.],
            )
        return self._verts
