from ..mixins import Part

from .fireplace_children import Floor
from .fireplace_children import Wall0


class Fireplace(Part):

    children = (
        Floor,
        Wall0,
    )

    name = 'Fireplace'
