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
    "author" : "Goodluck Focus", #inspired by Jason van Gumster (Fweeb)
    "description" : "Plays A Tune on Frame Render Completion or render error/cancelled",
    "blender" : (2, 81, 0),
    "version" : (0, 0, 1),
    "location" : "Render Settings > Render Tune",
    "warning" : "",
    "category" : "Render"
}

import bpy
from .rendertune_panel import renderTune_panel
from .rendertune import tuneProps, play_tune

#TODO Add A function that allows you to right click on a button and link to documentation
#TODO Conform this code to latest blender standard i.e  bpy.utils.register_classes_factory()
def register():
    bpy.utils.register_class(tuneProps)
    bpy.utils.register_class(renderTune_panel)
    bpy.types.RenderSettings.music_handle = None
    bpy.app.handlers.render_complete.append(play_tune)

def unregister():
    bpy.utils.unregister_class(tuneProps)
    bpy.utils.unregister_class(renderTune_panel)
    bpy.app.handlers.render_complete.remove(play_tune)