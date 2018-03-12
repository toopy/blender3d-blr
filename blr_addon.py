import logging
import bpy
import blr.cmd

bl_info = {
    "name": "BLR",
    "category": "Development",
}

logger = logging.getLogger(__name__)


class BlrMixin(bpy.types.Operator):
    bl_idname = None
    bl_label = None
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        blr.cmd.run(context, self)
        return {'FINISHED'}


class BlrAll(BlrMixin):
    bl_idname = "development.blr_all"
    bl_label = "BLR All Addon"


class BlrFloor0(BlrMixin):
    bl_idname = "development.blr_floor0"
    bl_label = "BLR Floor0 Addon"


class BlrFloor1(BlrMixin):
    bl_idname = "development.blr_floor1"
    bl_label = "BLR Floor1 Addon"


class BlrFloor2(BlrMixin):
    bl_idname = "development.blr_floor2"
    bl_label = "BLR Floor2 Addon"


def register():
    bpy.utils.register_class(BlrAll)
    bpy.utils.register_class(BlrFloor0)
    bpy.utils.register_class(BlrFloor1)
    bpy.utils.register_class(BlrFloor2)


def unregister():
    bpy.utils.unregister_class(BlrAll)
    bpy.utils.unregister_class(BlrFloor0)
    bpy.utils.unregister_class(BlrFloor1)
    bpy.utils.unregister_class(BlrFloor2)


if __name__ == "__main__":
    register()
