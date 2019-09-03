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

      layout.prop(addon_prefs, "tuneEnabler")
      layout.label(text = "Comming Soon: Tune location preference")  #TODO adding functionality to let the user select his/her tune of preference
      layout.label(text = "Comming Soon: Volume Control")  #TODO Adding volume control functionality if possible
      layout.prop(context.object, "tuneVolume")
      layout.label(text = "Comming Soon: Render Error ALERT") #TODO Add tune to play when render error occurs e.g out of disk space
      