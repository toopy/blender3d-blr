from ..mixins import Part

# from .kitchen_children import Canopy0
from .kitchen_children import Door0
from .kitchen_children import Door1
from .kitchen_children import Shelf0
from .kitchen_children import Shelf1
from .kitchen_children import Shelf2
from .kitchen_children import Shelf3
from .kitchen_children import Smeg
from .kitchen_children import Wall0
from .kitchen_children import Wall1
from .kitchen_children import Wall2
from .kitchen_children import Wood0


class Kitchen(Part):

    children = (
        # Canopy0,
        Door0,
        Door1,
        Shelf0,
        Shelf1,
        Shelf2,
        Shelf3,
        Smeg,
        Wall0,
        Wall1,
        Wall2,
        Wood0,
    )
    name = 'Kitchen'
    position = (
        3.,
        4.5,
        0.,
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [0.,  3.5, 0.],
                # >
                [3.,  3.5, 0.],
                [3.,  0,    0.],
                # <
                [1.5, 0,    0.],
                [1.5, .55,   0.],
                # <
                [1.,  .55,   0.],
                [1.,  .45,  0.],
                # <
                [.2,  .45,  0.],
                [.2,  .55,   0.],
                # <
                [.05, .55,   0.],
                [.05, 2.65, 0.],
                # <
                [0.,  2.65, 0.],
            )
        return self._verts
