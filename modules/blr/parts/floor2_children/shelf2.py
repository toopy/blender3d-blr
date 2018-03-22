from blr.parts.mixins import Part


class Shelf2(Part):

    color = (
        .5,
        .3,
        .0,
    )
    name = 'Shelf2'
    position = (
        2.65,
        3.1,
        1.18,
    )
    translate = (
        0.,
        0.,
        .02,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0., 0.,   0.],
                [0., 3.18, 0.],
                # <
                [.3, 3.18, 0.],
                [.3, 3.1,  0.],
                # <
                [.4, 3.1,  0.],
                [.4, 1.9,  0.],
                # >
                [.3, 1.9,  0.],
                [.3, 1.8,  0.],
                # <
                [.4, 1.8, 0.],
                [.4, 0.,  0.],
            )
        return self._verts
