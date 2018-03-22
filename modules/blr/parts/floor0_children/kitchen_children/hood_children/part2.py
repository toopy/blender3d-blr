from blr.parts.mixins import Part


class Part2(Part):

    name = 'Part2'
    position = (
        0.,
        0.,
        .09,
    )
    translate = (
        0.,
        0.,
        .8,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0.25, .17, 0.],
                [0.25, .43, 0.],
                # >
                [.5,  .43,  0.],
                [.5,  .17,  0.],
            )
        return self._verts
