from .floor2_children import Beam0
from .floor2_children import Beam1
from .floor2_children import Beam2
from .floor2_children import Beam3
from .floor2_children import Canopy0
from .floor2_children import Floor0
from .floor2_children import Floor1
from .floor2_children import Shelf0
from .floor2_children import Shelf1
from .floor2_children import Shelf2
from .floor2_children import Shelf3
from .floor2_children import Shelf4
from .floor2_children import Shelf5
from .floor2_children import Wall0
from .floor2_children import Wall1
from .floor2_children import Wall2
from .floor2_children import Wall3
from .floor2_children import Wall4
from .floor2_children import Wall5
from .floor2_children import Wall6
from .floor2_children import Wall7
from .floor2_children import Wall8
from .mixins import Part


class Floor2(Part):

    children = (
        Beam0,
        Beam1,
        Beam2,
        Beam3,
        Canopy0,
        Floor0,
        Floor1,
        Shelf0,
        Shelf1,
        Shelf2,
        Shelf3,
        Shelf4,
        Shelf5,
        Wall0,
        Wall1,
        Wall2,
        Wall3,
        Wall4,
        Wall5,
        Wall6,
        Wall7,
        Wall8,
    )
    name = 'Floor2'
