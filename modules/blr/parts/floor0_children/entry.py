from ..mixins import Part

from .entry_children import Wood0
from .entry_children import Wood1
from .entry_children import Wood2
from .entry_children import Wood3
from .entry_children import Wood4
from .entry_children import Wood5


class Entry(Part):

    children = (
        Wood0,
        Wood1,
        Wood2,
        Wood3,
        Wood4,
        Wood5,
    )
    color = (
        .8,
        .8,
        .8,
    )
    name = 'Entry'
    position = (
        3.,
        2.,
        0.
    )

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # .
                [.05, 0.,   0.],
                [.05, 1.1,  0.],
                # <
                [0.,  1.1,  0.],
                [0.,  1.9,  0.],
                # >
                [.05, 1.9,  0.],
                [.05, 2.95, 0.],
                # >
                [.2,  2.95, 0.],
                [.2,  3.,   0.],
                # >
                [1.,  3.,   0.],
                [1.,  2.95, 0.],
                # >
                [1.4, 2.95, 0.],
                [1.4, 1.5,  0.],
                # >
                [2.,  1.5,  0.],
                [2.,  1.3,  0.],
                # <
                [1.7, 1.3,  0.],
                [1.7, .9,   0.],
                # >
                [1.75, .9,  0.],
                [1.75, .1,  0.],
                # <
                [1.7,  .1,  0.],
                [1.7,  0.,  0.],
            )
        return self._verts
