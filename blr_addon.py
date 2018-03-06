import logging
import bpy
import blr.cmd

bl_info = {
    "name": "BLR",
    "category": "Development",
}

logger = logging.getLogger(__name__)


class Blr(bpy.types.Operator):
    """Run the BLR Addon"""
    bl_idname = "development.blr"
    bl_label = "BLR Addon"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        blr.cmd.run()
        return {'FINISHED'}

def register():
    bpy.utils.register_class(Blr)


def unregister():
    bpy.utils.unregister_class(Blr)


if __name__ == "__main__":
    register()
