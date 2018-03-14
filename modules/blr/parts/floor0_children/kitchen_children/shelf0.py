from ...mixins import Part


class Shelf0(Part):

    name = 'Shelf0'
    position = (
        2.3,
        2.8,
        1.7,
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
                [.7, .6, 0.],
                [.7, 0., 0.],
            )
        return self._verts
