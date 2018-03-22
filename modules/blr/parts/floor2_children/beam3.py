from blr.parts.mixins import Part


class Beam3(Part):

    color = (
        .5,
        .3,
        .0,
    )
    name = 'Beam3'
    position = (
        0.5,
        6.25,
        0.4,
    )
    translate = (
        0.,
        0.,
        .38,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0., 0.,    0.],
                [0., 0.05,  0.],
                # >
                [.05, 0.05, 0.],
                [.05, 0.,   0.],
            )
        return self._verts
