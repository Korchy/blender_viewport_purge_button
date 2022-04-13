# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_viewport_purge_button

import bpy
from bpy.props import BoolProperty
from bpy.types import Operator
from bpy.utils import register_class, unregister_class


class VIEWPORT_PURGE_BUTTON_OT_purge(Operator):
    bl_idname = 'viewport_purge_button.purge'
    bl_label = 'Purge'
    bl_description = 'Clear all orphaned data-blocks without any users from the file'
    bl_options = {'REGISTER', 'UNDO'}

    do_local_ids: BoolProperty(
        default=True
    )
    do_linked_ids: BoolProperty(
        default=True
    )
    do_recursive: BoolProperty(
        default=False
    )

    def execute(self, context):
        # execute purge operator
        if context.preferences.addons[__package__].preferences.confirm:
            return bpy.ops.outliner.orphans_purge(
                'INVOKE_DEFAULT',
                do_local_ids=self.do_local_ids,
                do_linked_ids=self.do_linked_ids,
                do_recursive=self.do_recursive
            )
        else:
            return bpy.ops.outliner.orphans_purge(
                do_local_ids=self.do_local_ids,
                do_linked_ids=self.do_linked_ids,
                do_recursive=self.do_recursive
            )


def register():
    register_class(VIEWPORT_PURGE_BUTTON_OT_purge)


def unregister():
    unregister_class(VIEWPORT_PURGE_BUTTON_OT_purge)
