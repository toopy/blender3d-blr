from ....mixins import Part


class Front0(Part):

    name = 'Front0'
    position = (
        0.,
        0.01,
        0.02
    )
    translate = (
        0.,
        0.,
        1.20,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0.,  0.,  0.],
                [0.,  .58, 0.],
                # ^
                [.65, .58, 0.],
                [.65, 0.,  0.],
            )
        return self._verts
