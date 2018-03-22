from blr.parts.mixins import Part

from .hood_children import Part0
from .hood_children import Part1
from .hood_children import Part2


class Hood(Part):

    children = (
        Part0,
        Part1,
        Part2,
    )
    name = 'Hood'
    position = (
        2.5,
        1.35,
        1.525,
    )
