import logging
from mathutils import Vector

import bpy
import bmesh

logger = logging.getLogger(__name__)


class Part:

    children = None
    color = (
        .5,
        .5,
        .5,
    )
    is_diff = False
    name = None
    position = (
        0.,
        0.,
        0.,
    )
    translate = None

    _faces = None
    _material = None
    _mesh = None
    _obj = None
    _verts = None

    def __init__(self, context):
        self.context = context

    @property
    def faces(self):
        if not self._faces:
            num_verts = len(self.verts)
            face = [i for i in range(num_verts)]
            self._faces = [face]
        return self._faces

    @property
    def material(self):
        material_name = '{}-material'.format(self.name.lower())
        if not self._material and self.obj:
            self._material = bpy.data.materials.get(material_name)
        if not self._material and self.obj:
            self._material = bpy.data.materials.new(material_name)
            self._material.use_object_color = True
        self._material.diffuse_color = self.color
        return self._material

    @property
    def mesh(self):
        if not self._mesh and self.faces and self.verts:
            self._mesh = bpy.data.meshes.new(self.name)
            self._mesh.from_pydata(
                [self.move(p) for p in self.verts],
                [],
                self.faces
            )
        return self._mesh

    @property
    def obj(self):
        if not self._obj and self.mesh:
            self._obj = bpy.data.objects.new(self.name, self.mesh)
            bpy.context.scene.objects.link(self._obj)
        return self._obj

    @property
    def verts(self):
        return []

    def apply_diff(self, child):

        # prepare modifier
        mod_name = '{}-{}-bool-mod'.format(
            self.name.lower(),
            child.name.lower(),
        )
        mod_bool = self.obj.modifiers.new(mod_name, 'BOOLEAN')
        mod_bool.operation = 'DIFFERENCE'
        mod_bool.object = child.obj

        # apply the modifier.
        bpy.context.scene.objects.active = self.obj
        bpy.ops.object.modifier_apply(modifier=mod_name)

        # delete the child.
        child.obj.select = True
        bpy.ops.object.delete()

    def build(self):

        if self.obj:
            # select
            self.obj.select = True
            bpy.context.scene.objects.active = self.obj
            # colorize
            self.obj.active_material = self.material
            # extrude
            self.extrude()
            # deselect
            self.obj.select = False

        for child_cls in (self.children or []):
            child = child_cls(self.context)
            child.build()
            if not child.is_diff:
                continue
            self.apply_diff(child)

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
                "value": self.translate,
            }
        )

        bpy.ops.object.mode_set(mode=cur_mode)

    def move(self, pos):
        return [self.position[i] + v for i, v in enumerate(pos)]
