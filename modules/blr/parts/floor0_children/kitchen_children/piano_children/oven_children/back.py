from .....mixins import Part


class Back(Part):

    name = 'Back'
    position = (
        .59,
        .0,
        .80,
    )
    translate = (
        0.,
        0.,
        .05,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0.,   0.,  0.],
                [0.,   .7, 0.],
                # >
                [0.01, .7, 0.],
                [0.01, 0.,  0.],
            )
        return self._verts
