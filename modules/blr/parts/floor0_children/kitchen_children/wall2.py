from blr.parts.mixins import Part


class Wall2(Part):

    name = 'Wall2'
    position = (
        2.4,
        2.7,
        0.,
    )
    translate = (
        0.,
        0.,
        3.,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0.,  0., 0.],
                [0.,  .1, 0.],
                # ^
                [.6, .1, 0.],
                [.6, 0., 0.],
            )
        return self._verts
