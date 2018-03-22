from blr.parts.mixins import Part


class Shelf1(Part):

    name = 'Shelf1'
    position = (
        0.02,
        .1,
        .45,
    )
    translate = (
        0.,
        0.,
        .02,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0.,  0., 0.],
                [0.,  .6, 0.],
                # ^
                [.58, .6, 0.],
                [.58, 0., 0.],
            )
        return self._verts
