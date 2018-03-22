from blr.parts.mixins import Part


class Door0(Part):

    name = 'Door0'
    position = (
        0.,
        .1,
        .1025,
    )
    translate = (
        .02,
        0.,
        0.,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0.,  0., 0.],
                [0.,  .6, 0.],
                # ^
                [0., .6, 0.745],
                [0., 0., 0.745],
            )
        return self._verts
