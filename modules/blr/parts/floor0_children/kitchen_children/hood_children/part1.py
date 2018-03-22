from blr.parts.mixins import Part


class Part1(Part):

    name = 'Part1'
    position = (
        0.,
        0.,
        .03,
    )

    @property
    def faces(self):
        return [
            [0,  1,  5,  4],
            [1,  2,  6,  5],
            [2,  3,  7,  6],
            [3,  0,  4,  7],
        ]

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                #
                [0.,   0., 0.],
                [0.,   .6, 0.],
                #
                [.5,   .6, 0.],
                [.5,   0., 0.],
                #
                [0.25, .17, .06],
                [0.25, .43, .06],
                #
                [.5,   .43, .06],
                [.5,   .17, .06],
            )
        return self._verts
