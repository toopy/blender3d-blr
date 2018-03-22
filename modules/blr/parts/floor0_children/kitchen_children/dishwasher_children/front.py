from blr.parts.mixins import Part


class Front(Part):

    name = 'Front'
    position = (
        0.,
        0.,
        0.05
    )
    translate = (
        0.,
        0.,
        .79,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0., 0., 0.],
                [0., .6, 0.],
                # ^
                [.6, .6, 0.],
                [.6, 0., 0.],
            )
        return self._verts
