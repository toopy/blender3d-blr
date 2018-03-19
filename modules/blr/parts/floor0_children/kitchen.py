from ..mixins import Part

from .kitchen_children import Basin
from .kitchen_children import Canopy0
from .kitchen_children import Dishwasher
from .kitchen_children import Door0
from .kitchen_children import Door1
from .kitchen_children import Door2
from .kitchen_children import Door3
from .kitchen_children import Door4
from .kitchen_children import Door5
from .kitchen_children import Door6
from .kitchen_children import Piano
from .kitchen_children import Shelf0
from .kitchen_children import Shelf1
from .kitchen_children import Shelf2
from .kitchen_children import Shelf3
from .kitchen_children import Shelf4
from .kitchen_children import Shelf5
from .kitchen_children import Shelf6
from .kitchen_children import Shelf7
from .kitchen_children import Shelf8
from .kitchen_children import Shelf9
from .kitchen_children import Shelf10
from .kitchen_children import Shelf11
from .kitchen_children import Shelf12
from .kitchen_children import Shelf13
from .kitchen_children import Shelf14
from .kitchen_children import Shelf15
from .kitchen_children import Shelf16
from .kitchen_children import Shelf17
from .kitchen_children import Shelf18
from .kitchen_children import Smeg
from .kitchen_children import Wall0
from .kitchen_children import Wall1
from .kitchen_children import Wall2
from .kitchen_children import Wall3
from .kitchen_children import Wall4
from .kitchen_children import Wood0
from .kitchen_children import Wood1
from .kitchen_children import Wood2


class Kitchen(Part):

    children = (
        Basin,
        Canopy0,
        Dishwasher,
        Door0,
        Door1,
        Door2,
        Door3,
        Door4,
        Door5,
        Door6,
        Piano,
        Shelf0,
        Shelf1,
        Shelf2,
        Shelf3,
        Shelf4,
        Shelf5,
        Shelf6,
        Shelf7,
        Shelf8,
        Shelf9,
        Shelf10,
        Shelf11,
        Shelf12,
        Shelf13,
        Shelf14,
        Shelf15,
        Shelf16,
        Shelf17,
        Shelf18,
        Smeg,
        Wall0,
        Wall1,
        Wall2,
        Wall3,
        Wall4,
        Wood0,
        Wood1,
        Wood2,
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
