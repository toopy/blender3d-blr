from blr.parts.mixins import Part


class Back(Part):

    name = 'Back'
    position = (
        0.15,
        0.,
        0.,
    )
    translate = (
        0.,
        0.,
        1.68,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0.,  0., 0.],
                [0.,  .6, 0.],
                # ^
                [.65, .6, 0.],
                [.65, 0., 0.],
            )
        return self._verts
