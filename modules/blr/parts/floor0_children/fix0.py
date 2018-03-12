from ..mixins import Part


class Fix0(Part):

    color = (
        .8,
        .8,
        .0,
    )
    name = 'Fix0'
    position = (
        4.,
        4.55,
        0.,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0., .4, 0.],
                [0., .5, 0.],
                # >
                [.5, .5, 0.],
                [.5, 0., 0.],
                # <
                [.4, 0., 0.],
                [.4, 0.4, 0.],
            )
        return self._verts
