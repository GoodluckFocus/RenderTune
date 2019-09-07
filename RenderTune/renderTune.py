import bpy, os, aud
from bpy.app.handlers import persistent

#function that handles(play) audio when render is complete
#attributes the outerspace class of blender "aud"
@persistent
def play_tune(scene):
    handle = bpy.types.RenderSettings.music_handle
    addon_prefs = bpy.context.preferences.addons[__package__].preferences
    
    #checks if render is complete
    if addon_prefs.tuneEnabler:
        device = aud.Device()
        device.volume=addon_prefs.tuneVol
        tunePlay = aud.Sound.file(addon_prefs.tuneLocation)
        bpy.types.RenderSettings.music_handle = device.play(tunePlay)
    #TODO Logic for when render results to error to play the tune
    if addon_prefs.errorTune:
        device = aud.Device()
        device.volume = addon_prefs.tuneVol
        tunePlay = aud.Sound.file(addon_prefs.errorTuneLocation)
        bpy.types.RenderSettings.music_handle = device.play(tunePlay)

#class to locate the tune location as well as defining the properties for the tune file and checkbox
class tuneProps(bpy.types.AddonPreferences):
    bl_idname = __package__
    tuneloc = bpy.path.abspath(os.path.dirname(__file__))  #TODO Make this variable for user insertion

    errorTuneLocation: bpy.props.StringProperty(
        name = "Error Tune",
        description = "Alert Tune when error there is an error",
        subtype = 'FILE_PATH',
        default = tuneloc + "/error.wav" ) # error tune location

    tuneLocation: bpy.props.StringProperty(
        name = "The Tune",
        description = "Alert Tune when Render completes",
        subtype = 'FILE_PATH',
        default = tuneloc + "/tune.mp3") # alert tune location
   
    tuneEnabler: bpy.props.BoolProperty(
        name = "Alert Render Complete",
        description = "Enable or Disable Tune Play on Render Completion",
        default = True)
    
    errorTune: bpy.props.BoolProperty(
        name = "Alert Render Error",
        description = "Enable or Disable error tune play when an error occurs while rendering",
        default = True)

    tuneVol : bpy.props.FloatProperty(
        name = "Volume",
        description = "Controls the Volume of the tune",
        default = 0.01)

