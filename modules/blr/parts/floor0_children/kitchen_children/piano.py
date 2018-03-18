from ...mixins import Part

from .piano_children import Oven


class Piano(Part):

    children = (
        # Door0,
        # Foot0,
        # Foot1,
        # Foot2,
        # Foot2,
        Oven,
        # Plate,
    )
    color = (
        1.,
        1.,
        1.,
    )
    name = 'Piano'
    position = (
        2.4,
        1.3,
        0.,
    )
