from ....mixins import Part


class Diff0(Part):

    is_diff = True
    name = 'Diff0'
    position = (
        .02,
        .02,
        .02,
    )
    translate = (
        .5,
        0.,
        0.,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0.,  0.,  0.],
                [0.,  .96, 0.],
                # >
                [0.,  .96, 0.96],
                [0.,  0.,  0.96],
            )
        return self._verts
