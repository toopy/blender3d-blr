from ....mixins import Part


class Back(Part):

    name = 'Back'
    position = (
        0.02,
        0.,
        0.,
    )
    translate = (
        0.,
        0.,
        .85,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0., 0., 0.],
                [0., .6, 0.],
                # ^
                [.58, .6, 0.],
                [.58, 0., 0.],
            )
        return self._verts
