from blr.parts.mixins import Part

from .block3_children import Wood0


class Block3(Part):

    children = (
        Wood0,
    )
    name = 'Block3'
    position = (
        0.,
        4.,
        0.,
    )
