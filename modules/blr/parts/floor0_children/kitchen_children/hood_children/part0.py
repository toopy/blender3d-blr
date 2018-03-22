from blr.parts.mixins import Part


class Part0(Part):

    name = 'Part0'
    translate = (
        0.,
        0.,
        .03,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0,  0., 0.],
                [0,  .6, 0.],
                # >
                [.5, .6, 0.],
                [.5, 0., 0.],
            )
        return self._verts
