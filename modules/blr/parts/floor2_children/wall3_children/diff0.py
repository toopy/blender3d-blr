from ...mixins import Part


class Diff0(Part):

    is_diff = True
    name = 'Diff0'
    translate = (
        0.,
        0.,
        1.,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [-0.1, 0., 0.],
                [-0.1, 4., 2.8],
                # >
                [3.,   4., 2.8],
                [3.,   0., 0.],
            )
        return self._verts
