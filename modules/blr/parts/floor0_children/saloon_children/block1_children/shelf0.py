from blr.parts.mixins import Part


class Shelf0(Part):

    name = 'Shelf0'
    position = (
        -.25,
        0.,
        .7,
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
                [0., 0.,   0.],
                [0., 1.3,  0.],
                # >
                [.22, 1.49,  0.],
                # >
                [.5, 1.49, 0.],
                [.5, 0.,   0.],
            )
        return self._verts
