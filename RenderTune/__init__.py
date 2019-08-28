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
    "name" : "Render Tune",
    "author" : "Goodluck Focus",
    "description" : "Plays A Tune on Frame Render Completion",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Render"
}

import bpy
from .renderTune_panel import renderTune_panel
from .renderTune_op import RENDERTUNE_OT_Operator


#TODO convert this to new code using bpy.utils.register_classes_factory()
def register():
    bpy.types.Scene.render_alert = bpy.props.BoolProperty(
        name="",
        description="Plays a tune when Render Completes",
        default = False)
    bpy.utils.register_class(renderTune_panel)
    bpy.utils.register_class (RENDERTUNE_OT_Operator)


def unregister():
    bpy.utils.unregister_class(renderTune_panel)
    bpy.utils.unregister_class (RENDERTUNE_OT_Operator)
    del bpy.types.Scene.render_alert