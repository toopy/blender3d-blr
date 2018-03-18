from ...mixins import Part


class Basin(Part):

    name = 'Basin'
    position = (
        2.45,
        .1,
        .90,
    )

    @property
    def faces(self):
        return [
            [0,  1,  5,  4],
            [1,  2,  6,  5],
            [2,  3,  7,  6],
            [3,  0,  4,  7],
            [4,  5,  9,  8],
            [5,  6,  10, 9],
            [6,  7,  11, 10],
            [7,  4,  8,  11],
            [8,  9,  13, 12],
            [9,  10, 14, 13],
            [10, 11, 15, 14],
            [11, 8,  12, 15],
        ]

    @property
    def verts(self):
        if not self._verts:
            self._verts = (
                # [1]
                [0.,  0.,  0.],
                [0.,  .57, 0.],
                [0.5, .57, 0.],
                [0.5, 0.,  0.],
                # [2]
                [0.02, .02, 0.],
                [0.02, .55, 0.],
                [0.42, .55, 0.],
                [0.42, .02,  0.],
                # [3]
                [0.025, .025, -.15],
                [0.025, .55,  -.15],
                [0.415, .55,  -.15],
                [0.415, .025, -.15],
                # [4]
                [0.245, .205, -.15],
                [0.245, .255, -.15],
                [0.295, .255, -.15],
                [0.295, .205, -.15],
            )
        return self._verts
