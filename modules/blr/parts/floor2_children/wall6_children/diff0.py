from ...mixins import Part


class Diff0(Part):

    is_diff = True
    name = 'Diff0'
    translate = (
        2.,
        0.,
        0.,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [2., 0., 0.],
                # ^
                [2., 4., 2.8],
                [2., 8., 0.],
                # ^^
                [2., 8., 3.],
                [2., 0., 3.],
            )
        return self._verts
