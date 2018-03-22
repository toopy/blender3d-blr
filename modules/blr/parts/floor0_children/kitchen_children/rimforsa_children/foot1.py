from blr.parts.mixins import Part


class Foot1(Part):

    name = 'Foot1'
    position = (
        0.61,
        0.,
        0.,
    )
    translate = (
        0.,
        0.,
        .8,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0.,   0.,  0.],
                [0.,   .04, 0.],
                # >
                [0.04, .04, 0.],
                [0.04, 0.,  0.],
            )
        return self._verts
