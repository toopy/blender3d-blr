from ....mixins import Part


class Diff2(Part):

    is_diff = True
    name = 'Diff2'
    position = (
        -.02,
        1.28,
        .06,
    )
    translate = (
        0.,
        0.,
        1.88,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0,  0.,   0.],
                [0,  0.55, 0.],
                # >
                [.1, .55, 0.],
                [.1, 0.,  0.],
            )
        return self._verts
