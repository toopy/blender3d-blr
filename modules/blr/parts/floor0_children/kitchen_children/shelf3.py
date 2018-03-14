from ...mixins import Part


class Shelf3(Part):

    name = 'Shelf3'
    position = (
        2.3,
        2.8,
        2.52,
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
