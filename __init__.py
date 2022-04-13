# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_viewport_purge_button

from . import vpb_ops
from . import vpb_ui
from . import vpb_preferences
from .addon import Addon

bl_info = {
    'name': 'Viewport Purge Button',
    'category': 'All',
    'author': 'Nikita Akimov',
    'version': (1, 0, 0),
    'blender': (2, 93, 0),
    'location': '3D Viewport header',
    'doc_url': 'https://b3d.interplanety.org/en/blender-add-on-viewport-purge-button/',
    'tracker_url': 'https://b3d.interplanety.org/en/blender-add-on-viewport-purge-button/',
    'description': 'Adds the \"Purge\" button to the 3D Viewport header'
}


def register():
    if not Addon.dev_mode():
        vpb_preferences.register()
        vpb_ops.register()
        vpb_ui.register()
    else:
        print('It seems you are trying to use the dev version of the '
              + bl_info['name']
              + ' add-on. It may work not properly. Please download and use the release version')


def unregister():
    if not Addon.dev_mode():
        vpb_ui.unregister()
        vpb_ops.unregister()
        vpb_preferences.unregister()


if __name__ == '__main__':
    register()
