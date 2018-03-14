from ...mixins import Part


class Beam0(Part):

    name = 'Beam0'
    position = (
        .15,
        0.,
        0.,
    )
    translate = (
        0.,
        0.,
        3.2,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0., 0., 0.],
                [0., .1, 0.],
                # >
                [.1, .1, 0.],
                [.1, 0., 0.],
            )
        return self._verts
