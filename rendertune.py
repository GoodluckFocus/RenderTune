import bpy, os, aud
from bpy.app.handlers import persistent


@persistent
def play_tune(scene):
    handle = bpy.types.RenderSettings.music_handle
    addon_prefs = bpy.context.preferences.addons[__package__].preferences
    
    #TODO Logic for when render results to error to play the tune
    #checks if the checkbox is true then gets the tune location the checks if render is complete
    #if yes plays the render tune is no plays the error tune
    #whatif i dont want render tune but i want render error tune???
    if addon_prefs.tuneEnabler:
        device = aud.Device()
        device.volume=addon_prefs.tuneVol
        tunePlay = aud.Sound.file(addon_prefs.tuneLocation)
        errorPlay = aud.Sound.file(addon_prefs.errorTuneLocation)
        handle = device.play(errorPlay)
    
   
class tuneProps(bpy.types.AddonPreferences):
    """Contains Addon Properties"""
    bl_idname = __package__
    tuneloc = bpy.path.abspath(os.path.dirname(__file__))

    #Property for Render Error Alert Tune location
    errorTuneLocation: bpy.props.StringProperty(
        name = "Error Tune",
        description = "Alert Tune when error there is an error/cancellation",
        subtype = 'FILE_PATH',
        default = tuneloc + "/error.wav" )

    #Property for Complete Render Tune location
    tuneLocation: bpy.props.StringProperty(
        name = "The Tune",
        description = "Alert Tune when Render completes",
        subtype = 'FILE_PATH',
        default = tuneloc + "/tune.mp3")
   
    # Checkbox to enable the complete render tune play
    tuneEnabler: bpy.props.BoolProperty(
        name = "Alert Render Complete",
        description = "Enable or Disable Tune Play on Render Completion",
        default = True)
    
     # Checkbox to enable the render error tune play
    errorTune: bpy.props.BoolProperty(
        name = "Alert Render Error",
        description = "Enable or Disable error tune play when an error occurs while rendering",
        default = True)

    # Volume slider control
    tuneVol : bpy.props.FloatProperty(
        name = "Volume",
        description = "Controls the Volume of the tune",
        default = 1)

