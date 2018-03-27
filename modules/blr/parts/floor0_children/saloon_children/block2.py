from blr.parts.mixins import Part

from .block2_children import Wood0


class Block2(Part):

    children = (
        Wood0,
    )
    name = 'Block2'
    position = (
        0.,
        .5,
        0.,
    )
