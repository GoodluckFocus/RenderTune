# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "RenderTune",
    "author" : "Goodluck Focus",
    "description" : "Plays An Alert Tune when Render Completes",
    "blender" : (4, 4, 0),
    "version" : (1, 0, 0),
    "location" : "Render Settings > Render Tune",
    "warning" : "",
    "category" : "Render",
    "Date":"2025"
}
#TODO Confirm the code to latest blender documentation and reliable for the next version of blender 4.2

import bpy
from .rendertune_panel import RENDER_PT_rendertune
from .rendertune import AlertProps, render_complete, render_cancel

#TODO Add the addon on the Render Top Bar Menu on Render Tap
#def topbar_menu(self, context):
    #self.layout.operator(rendertune.bl_idname)
 #   self.layout.operator(tuneProps.bl_idname)


def register():
    bpy.utils.register_class(RENDER_PT_rendertune)
    bpy.utils.register_class(AlertProps)
    bpy.types.RenderSettings.music_handle = None
    bpy.app.handlers.render_complete.append(render_complete)
    bpy.app.handlers.render_cancel.append(render_cancel)
   # bpy.types.TOPBAR_MT_render.append(topbar_menu)

def unregister():
    bpy.utils.unregister_class(RENDER_PT_rendertune)
    bpy.utils.unregister_class(AlertProps)
    bpy.app.handlers.render_complete.remove(render_complete)
    bpy.app.handlers.render_cancel.remove(render_cancel)
   # bpy.types.TOPBAR_MT_render.remove(topbar_menu)
