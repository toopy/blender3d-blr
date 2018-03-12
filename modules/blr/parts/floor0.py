from .floor0_children import Entry
from .floor0_children import Fireplace
from .floor0_children import Fix0
from .floor0_children import Fix1
from .floor0_children import Fix2
from .floor0_children import Kitchen
from .floor0_children import Saloon
from .floor0_children import Wc
from .floor0_children import Wood0
from .mixins import Part


class Floor0(Part):

    children = (
        Entry,
        Fireplace,
        Fix0,
        Fix1,
        Fix2,
        Kitchen,
        Saloon,
        Wc,
        Wood0,
    )
    name = 'Floor0'
