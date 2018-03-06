import logging

import bpy
import bmesh

from .mixins import Part

logger = logging.getLogger(__name__)


class Floor0(Part):

    name = 'Floor 0'

    @property
    def faces(self):
        return (
            (0, 1),
            (1, 2),
            (2, 3),
            (3, 0),
        )

    @property
    def verts(self):
        return [
            self.loc(l)
            for l in (
                (0., 2., 0.),
                (2., 2., 0.),
                (2., 0., 0.),
                (0., 0., 0.),
            )
        ]
