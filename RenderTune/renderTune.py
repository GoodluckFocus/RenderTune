import bpy, os, aud
from bpy.app.handlers import persistent

#function that handles(play) audio when render is complete
#attributes the outerspace class of blender "aud"
@persistent
def play_tune(scene):
    handle = bpy.types.RenderSettings.music_handle
    addon_prefs = bpy.context.preferences.addons[__package__].preferences
    
    if addon_prefs.tuneEnabler:
        device = aud.Device()
        #device.volume=
        tunePlay = aud.Sound.file(addon_prefs.tuneLocation)
        bpy.types.RenderSettings.music_handle = device.play(tunePlay)

#Proposed volume control
device = aud.Device()
device.volume=0.01   # variable to be controlled from panel

#class to locate the tune location as well as defining the properties for the tune file and checkbox
class tuneProps(bpy.types.AddonPreferences):
    bl_idname = __package__
    tuneloc = bpy.path.abspath(os.path.dirname(__file__))  #TODO Make this variable for user insertion

    tuneLocation: bpy.props.StringProperty(
        name = "The Tune",
        description = "Alert Tune when Render completes",
        subtype = 'FILE_PATH',
        default = tuneloc + "/tune.mp3") #a royalty free soundFx
   
    tuneEnabler: bpy.props.BoolProperty(
        name = "Alert Render Tune",
        description = "Enable or Disable Tune Play on Render Completion",
        default = True)

    tuneVolume = bpy.props.FloatProperty(
        name = "Volume",
        default = 1,
        description = "Sets the Volume of the Tune")