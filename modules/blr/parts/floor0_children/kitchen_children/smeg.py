from ...mixins import Part

from .smeg_children import Back
from .smeg_children import Front0
from .smeg_children import Front1


class Smeg(Part):

    children = (
        Back,
        Front0,
        Front1,
    )
    color = (
        .8,
        .8,
        .0,
    )
    name = 'Smeg'
    position = (
        2.2,
        2.8,
        0.,
    )
