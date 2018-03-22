from blr.parts.mixins import Part

from .fireplace_children import Floor
from .fireplace_children import Wall0


class Fireplace(Part):

    children = (
        Floor,
        Wall0,
    )
    color = (
        .8,
        .8,
        .0,
    )
    name = 'Fireplace'
    position = (
        0.,
        3.2,
        0.,
    )
