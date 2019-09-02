import bpy, os, aud
from bpy.app.handlers import persistent

#function that handles(play) audio when render is complete
#attributes the outerspace class of blender "aud"
@persistent
def end_music(scene):
    handle = bpy.types.RenderSettings.music_handle
    addon_prefs = bpy.context.preferences.addons[__package__].preferences
    
    if addon_prefs.use_end:
        device = aud.Device()
        endMusic = aud.Sound.file(addon_prefs.endfile)
        bpy.types.RenderSettings.music_handle = device.play(endMusic)

#class to locate the tune location as well as defining the properties for the tune file and checkbox
class tuneProps(bpy.types.AddonPreferences):
    bl_idname = __package__
    tuneloc = bpy.path.abspath(os.path.dirname(__file__))  #TODO Make this variable for user insertion

    endfile: bpy.props.StringProperty(
        name = "The Tune",
        description = "Alert Tune when Render completes",
        subtype = 'FILE_PATH',
        default = tuneloc + "/tune.mp3") #a royalty free soundFx
   
    use_end: bpy.props.BoolProperty(
        name = "Alert Render Tune",
        description = "Enable or Disable Tune Play on Render Completion",
        default = True)