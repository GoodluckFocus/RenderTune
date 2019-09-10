import bpy

class renderTune_panel(bpy.types.Panel):
    """ Creates A Render Tune Panel in the Render Context of the Properties Window"""
    bl_idname = "RENDER_PT_Panel"
    bl_label = "Render Tune"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "render"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
      addon_prefs =bpy.context.preferences.addons[__package__].preferences
      layout = self.layout

      layout.prop(addon_prefs, "tuneEnabler") #Render Complete tune
      layout.prop(addon_prefs, "errorTune") # Render Error tune
      layout.prop(addon_prefs, "tuneVol")  #Volume dialing Slide
      