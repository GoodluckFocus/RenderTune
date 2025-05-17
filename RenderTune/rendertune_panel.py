import bpy

class RENDER_PT_rendertune(bpy.types.Panel):
    """Creates A Render Tune Panel in the Render Context of the Properties Window"""
    bl_idname = 'RENDER_PT_rendertune'
    bl_label = "Render Tune"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "render"
    bl_options = {'DEFAULT_CLOSED'}


    def draw(self, context):
        addon_prefs =bpy.context.preferences.addons[__package__].preferences
        layout = self.layout

        layout.prop(addon_prefs, "successAlert") #Render Complete tune
        layout.prop(addon_prefs, "errorAlert") #Render Error tune
        layout.prop(addon_prefs, "cancelAlert") #Render Cancellation Tune
        layout.prop(addon_prefs, "alertVol")  #Volume dialing Slide
