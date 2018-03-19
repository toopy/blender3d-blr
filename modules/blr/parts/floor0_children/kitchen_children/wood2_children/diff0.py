from ....mixins import Part


class Diff0(Part):

    is_diff = True
    name = 'Diff0'
    position = (
        .05,
        .015,
        -.01,
    )
    translate = (
        0.,
        0.,
        0.1,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0.,  0.,   0.],
                [0.,  .57,  0.],
                # >
                [0.5, 0.57, 0.],
                [0.5, 0.,   0.],
            )
        return self._verts
