from blr.parts.mixins import Part


class Door0(Part):

    name = 'Door0'
    position = (
        0.,
        0.0025,
        .1025,
    )
    translate = (
        0.,
        0.,
        .745,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0.,  0.,  0.],
                [0.,  .595, 0.],
                # ^
                [.02, 0.595, 0.],
                [.02, 0.,  0.],
            )
        return self._verts
