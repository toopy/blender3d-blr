from ..mixins import Part


class Beam0(Part):

    color = (
        .5,
        .3,
        .0,
    )
    name = 'Beam0'
    position = (
        2.95,
        3.,
        0,
    )
    translate = (
        0.,
        0.,
        2.,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0., 0., 0.],
                [0., .1, 0.],
                # >
                [0.1, .1, 0.],
                [0.1, 0., 0.],
            )
        return self._verts
