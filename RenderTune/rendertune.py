import bpy, os, aud
from bpy.app.handlers import persistent


@persistent
def play_tune(scene):
    handle = bpy.types.RenderSettings.music_handle
    addon_prefs = bpy.context.preferences.addons[__package__].preferences
    
    #TODO Create a logic for the 3 states
    # when render completes
    # when render is interrupted by error or cancelled
    if addon_prefs.tuneEnabler:
        device = aud.Device()
        device.volume=addon_prefs.tuneVol
        tunePlay = aud.Sound.file(addon_prefs.tuneLocation)
        interruptPlay = aud.Sound.file(addon_prefs.interruptLocation)
     #  handle = device.play(interruptPlay)  Interruption(cancel or error) tune play
        handle = device.play(tunePlay)



class tuneProps(bpy.types.AddonPreferences):
    """Contains Addon Properties"""
    bl_idname = __package__
    #tuneloc = bpy.path.abspath(os.path.dirname(__file__))
    tuneloc = bpy.path.abspath(os.path.dirname(__file__))

   

    #Render Complete tune location
    tuneLocation: bpy.props.StringProperty(
       name = "The Tune",
       description = "Alert Tune when Render Completes",
       subtype = 'FILE_PATH',
       default = tuneloc + "/tune.mp3"
    ) #type:ignore

    # Render Interruption tune location
    interruptLocation: bpy.props.StringProperty(
        name = "The Interruption Tune",
        description = "Alert Tune when Render Completes",
        subtype = 'FILE_PATH',
        default = tuneloc + "/error.wav"
    ) # type: ignore

    # Checkbox to enable the complete render tune play
    tuneEnabler: bpy.props.BoolProperty(
        name = "Alert Render Complete",
        description = "Enable or Disable Tune Play on Render Completion",
        default = True) #type:ignore
    
     # Checkbox to enable the render error tune play
    errorTune: bpy.props.BoolProperty(
        name = "Alert Render Error",
        description = "Enable or Disable error tune play when an error occurs while rendering",
        default = True) # type:ignore

    # Checkbox to enable the render cancellation tune play
    cancelTune: bpy.props.BoolProperty(
        name = "Alert Render Cancellation",
        description = "Enable or Disable error tune play when rendering is cancelled",
        default = True) #type:ignore

    # Volume slider control
    tuneVol : bpy.props.FloatProperty(
        name = "Volume",
        description = "Controls the Volume of the tune",
        default = 0.5,
        min = 0.3, soft_max = 1
        ) #type: ignore

 #TODO create a user customization tunes - user to enter his desired tunes for the three cases