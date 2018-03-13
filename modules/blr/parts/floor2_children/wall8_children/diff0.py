from ...mixins import Part


class Diff0(Part):

    is_diff = True
    name = 'Diff0'
    position = (
        -.1,
        -3.,
        -2.,
    )
    translate = (
        2.5,
        0.,
        0.,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0., 0., 0.],
                # ^
                [0., 4., 2.8],
                [0., 8., 0.],
                # ^^
                [0., 8., 3.5],
                [0., 0., 3.5],
            )
        return self._verts
