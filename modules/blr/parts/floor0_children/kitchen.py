from blr.parts.mixins import Part

from .kitchen_children import Block0
from .kitchen_children import Block1
from .kitchen_children import Block2
from .kitchen_children import Block3
from .kitchen_children import Block4
from .kitchen_children import Canopy0
from .kitchen_children import Dishwasher
from .kitchen_children import Hood
from .kitchen_children import Piano
from .kitchen_children import Rimforsa
from .kitchen_children import Smeg
from .kitchen_children import Wall0
from .kitchen_children import Wall1
from .kitchen_children import Wall2
from .kitchen_children import Wall3


class Kitchen(Part):

    children = (
        Block0,
        Block1,
        Block2,
        Block3,
        Block4,
        Canopy0,
        Dishwasher,
        Hood,
        Piano,
        Rimforsa,
        Smeg,
        Wall0,
        Wall1,
        Wall2,
        Wall3,
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
