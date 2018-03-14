from ....mixins import Part


class Diff3(Part):

    is_diff = True
    name = 'Diff3'
    position = (
        -.02,
        1.89,
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
