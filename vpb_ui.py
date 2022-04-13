# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_viewport_purge_button

from bpy.types import VIEW3D_HT_tool_header, VIEW3D_HT_header
from bpy.app import version
from bpy.app.handlers import persistent


@persistent
def viewport_purge_button_draw(self, context):
    layout = self.layout
    text = '' if context.preferences.addons[__package__].preferences.only_icon else 'Purge'
    layout.operator(
        operator='viewport_purge_button.purge',
        text=text,
        icon='TRASH'
    )


def register():
    if version < (3, 0, 0):
        VIEW3D_HT_header.prepend(viewport_purge_button_draw)
    else:
        VIEW3D_HT_tool_header.prepend(viewport_purge_button_draw)


def unregister():
    VIEW3D_HT_tool_header.remove(viewport_purge_button_draw)
