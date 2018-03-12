from ..mixins import Part


class Bedroom0(Part):

    color = (
        .9,
        .6,
        .0,
    )
    name = 'Bedroom0'
    position = (
        0.,
        0.,
        6.4,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # >
                [0.,   0.,  0.],
                [0.,   8., 0.],
                # <
                [2.95,   8.,  0.],
                [2.95,   0., 0.],
            )
        return self._verts
