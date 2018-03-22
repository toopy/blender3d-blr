from blr.parts.mixins import Part


class Wood0(Part):

    name = 'Wood0'
    position = (
        0.,
        0.,
        .85,
    )
    translate = (
        0.,
        0.,
        .05,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0., 0., 0.],
                [0., .7, 0.],
                # ^
                [.6, .7, 0.],
                [.6, 0., 0.],
            )
        return self._verts
