from ..mixins import Part


class Shelf4(Part):

    color = (
        .5,
        .3,
        .0,
    )
    name = 'Shelf4'
    position = (
        0.5,
        6.25,
        0.38,
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
                [0., 0.5, 0.],
                # <
                [2.05, 0.5, 0.],
                [2.05, 0.,  0.],
            )
        return self._verts
