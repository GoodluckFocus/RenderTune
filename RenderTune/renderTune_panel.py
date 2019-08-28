import bpy

class renderTune_panel(bpy.types.Panel):
    """ Creates A Render Tune Panel in the Render Context of the Properties Window"""
    """With Check box for Enabling or Not"""
    bl_idname = "RENDER_PT_Panel"
    bl_label = "Render Tune"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "render"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout=self.layout
        scene = context.scene
        layout.prop(scene, "render_alert")

    #TODO link to the Operator
    #TODO logic to check if the check box is ticked or Not