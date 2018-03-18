from ...mixins import Part

from .dishwasher_children import Back
from .dishwasher_children import Front


class Dishwasher(Part):

    children = (
        Back,
        Front,
    )
    color = (
        .8,
        .8,
        .0,
    )
    name = 'Dishwasher'
    position = (
        2.4,
        2.1,
        0.,
    )
