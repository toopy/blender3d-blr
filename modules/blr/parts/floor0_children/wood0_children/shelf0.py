from ...mixins import Part


class Shelf0(Part):

    angle = (
        0.,
        30.,
        0.,
    )
    name = 'Shelf0'
    position = (
        0.,
        .02,
        .35,
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
