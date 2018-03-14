from ...mixins import Part


class Shelf1(Part):

    angle = (
        0.,
        30.,
        0.,
    )
    name = 'Shelf1'
    position = (
        0.,
        .02,
        .70,
    )
    translate = (
        0.,
        0.,
        0.02,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0., 0.,  0.],
                [0., 1.16, 0.],
                # >
                [0.4, 1.16, 0.],
                [0.4, 0.,  0.],
            )
        return self._verts
