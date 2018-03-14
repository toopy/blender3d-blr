from ...mixins import Part


class Shelf0(Part):

    angle = (
        0.,
        25.,
        0.,
    )
    name = 'Shelf0'
    position = (
        .03,
        .02,
        .18,
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
                [0.34, 1.16, 0.],
                [0.34, 0.,  0.],
            )
        return self._verts
