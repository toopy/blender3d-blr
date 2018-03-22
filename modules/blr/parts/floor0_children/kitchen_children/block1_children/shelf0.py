from blr.parts.mixins import Part


class Shelf0(Part):

    name = 'Shelf0'
    position = (
        0.,
        0.,
        0.,
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
                [0., 0., 0.],
                [0., .6, 0.],
                # ^
                [.33, .6, 0.],
                [.33, 0., 0.],
            )
        return self._verts
