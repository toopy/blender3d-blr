import logging
from mathutils import Vector

import bpy
import bmesh

logger = logging.getLogger(__name__)


class Part:

    children = None
    name = None

    _mesh = None
    _obj = None

    def __init__(self, context, location=None):
        self.context = context
        self.location = location or (0, 0, 0)

    @property
    def faces(self):
        return []

    @property
    def mesh(self):
        if not self._mesh:
            self._mesh = bpy.data.meshes.new(self.name)
            self._mesh.from_pydata(self.verts, [], self.faces)
        return self._mesh

    @property
    def obj(self):
        if not self._obj:
            self._obj = bpy.data.objects.new(self.name, self.mesh)
            bpy.context.scene.objects.link(self._obj)
        return self._obj

    @property
    def translate(self):
        pass

    @property
    def verts(self):
        return []

    def build(self):

        # select
        self.obj.select = True
        bpy.context.scene.objects.active = self.obj

        # extrude
        self.extrude()

        # deselect
        self.obj.select = False

        for child in (self.children or []):
            child(self.context, location=self.location).build()

    def extrude(self):

        if not self.translate:
            return

        cur_mode = bpy.context.active_object.mode

        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_mode(type='FACE')

        bm = bmesh.new()
        bm.from_mesh(self.mesh)

        for face in bm.faces[:]:
            face.select = True

        bpy.ops.mesh.extrude_region_move(
            TRANSFORM_OT_translate={
                "value": self.translate
            }
        )

        bpy.ops.object.mode_set(mode=cur_mode)

    def loc(self, loc):
        return [self.location[i] + v for i, v in enumerate(loc)]
