from blr.parts.mixins import Part


class Diff3(Part):

    is_diff = True
    name = 'Diff3'
    position = (
        -.02,
        1.525,
        .025,
    )
    translate = (
        0.,
        0.,
        1.85,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0,  0.,   0.],
                [0,  0.45, 0.],
                # >
                [.1, .45, 0.],
                [.1, 0.,  0.],
            )
        return self._verts
