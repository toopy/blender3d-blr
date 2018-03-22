from blr.parts.mixins import Part

from .rimforsa_children import Drawer0
from .rimforsa_children import Drawer1
from .rimforsa_children import Foot0
from .rimforsa_children import Foot1
from .rimforsa_children import Foot2
from .rimforsa_children import Foot3
from .rimforsa_children import Step0
from .rimforsa_children import Step1
from .rimforsa_children import Wood0


class Rimforsa(Part):

    children = (
        Drawer0,
        Drawer1,
        Foot0,
        Foot1,
        Foot2,
        Foot3,
        Step0,
        Step1,
        Wood0,
    )
    color = (
        .9,
        .9,
        .9,
    )
    name = 'Rimforsa'
    position = (
        .05,
        .9,
        0.,
    )
