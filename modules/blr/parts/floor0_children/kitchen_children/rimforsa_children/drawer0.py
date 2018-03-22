from blr.parts.mixins import Part


class Drawer0(Part):

    name = 'Drawer0'
    position = (
        0.,
        0.0425,
        0.65,
    )
    translate = (
        0.,
        0.,
        .15,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0.,   0.,  0.],
                [0.,   0.55, 0.],
                # >
                [0.65, 0.55, 0.],
                [0.65, 0.,  0.],
            )
        return self._verts
