import bpy
import bmesh
from bpy_extras import object_utils


class Part:

    location = (0, 0, 0)
    name = None

    def __init__(self, context):
        self.context = context

    def build(self):
        mesh = bpy.data.meshes.new(self.name)
        mesh.from_pydata(self.verts, [], self.faces)
        mesh.update()
        # TODO: handle faces & color
        object_utils.object_data_add(self.context, mesh, operator=None)

    def create(self, mesh):
        raise NotImplementedError

    def loc(self, loc):
        return [self.location[i] + v for i, v in enumerate(loc)]
