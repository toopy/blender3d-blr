from .floor2_children import Bedroom0
from .mixins import Part


class Floor2(Part):

    children = (
        Bedroom0,
    )
    name = 'Floor2'
