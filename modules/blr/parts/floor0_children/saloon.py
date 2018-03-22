from blr.parts.mixins import Part

from .saloon_children import Wall0
from .saloon_children import Wall1
from .saloon_children import Wall2


class Saloon(Part):

    children = (
        Wall0,
        Wall1,
        Wall2,
    )
    color = (
        .8,
        .4,
        .0,
    )
    name = 'Saloon'

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # >
                [0.,   0.,  0.],
                [0.,   3.2, 0.],
                # fireplace
                [.8,   4.,  0.],
                [0.,   4.8, 0.],
                [0.,   8.,  0.],
                # >
                [2.95, 8.,  0.],
                # >
                [3.,   8.,  0.],
                [3.,   7.2, 0.],
                # <
                [2.95, 7.2, 0.],
                [2.95, 3.1, 0.],
                # >
                [3.,   3.1, 0.],
                [3.,   3.9, 0.],
                # <
                [2.95, 3.9, 0.],
                [2.95, 0.,  0.],
            )
        return self._verts
