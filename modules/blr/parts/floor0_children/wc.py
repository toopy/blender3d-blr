from blr.parts.mixins import Part


class Wc(Part):

    name = 'Wc'
    position = (
        4.75,
        2.,
        0.,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0.05, 0.,  0.],
                [0.05, .1,  0.],
                # <
                [0.,   .1,  0.],
                [0.,   .9,  0.],
                # >
                [0.05, .9,  0.],
                [0.05, 1.,  0.],
                # >
                [0.25, 1.,  0.],
                [0.25, 1.2, 0.],
                # >
                [1.25, 1.2, 0.],
                [1.25, 0.,  0.],
            )
        return self._verts
