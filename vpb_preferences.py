# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_viewport_purge_button

from bpy.types import AddonPreferences
from bpy.props import BoolProperty
from bpy.utils import register_class, unregister_class


class VIEWPORT_PURGE_BUTTON_preferences(AddonPreferences):
    bl_idname = __package__

    confirm: BoolProperty(
        name='Confirm message',
        default=True
    )
    only_icon: BoolProperty(
        name='Only Icon',
        default=False
    )

    def draw(self, context):
        layout = self.layout
        layout.prop(self, 'confirm')
        layout.prop(self, 'only_icon')


def register():
    register_class(VIEWPORT_PURGE_BUTTON_preferences)


def unregister():
    unregister_class(VIEWPORT_PURGE_BUTTON_preferences)
