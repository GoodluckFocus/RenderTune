import bpy, os, aud
from bpy.app.handlers import persistent


@persistent
def play_tune(scene):
    handle = bpy.types.RenderSettings.music_handle
    addon_prefs = bpy.context.preferences.addons[__package__].preferences
    
    if addon_prefs.tuneEnabler:
        device = aud.Device()
        device.volume=addon_prefs.tuneVol
        tunePlay = aud.Sound.file(addon_prefs.tuneLocation)
        handle = device.play(tunePlay)



class tuneProps(bpy.types.AddonPreferences):
    """Contains Addon Properties"""
    bl_idname = __package__
    tuneloc = bpy.path.abspath(os.path.dirname(__file__))

    tuneLocation: bpy.props.StringProperty(
        name = "The Tune",
        description = "Alert Tune when Render Completes",
        subtype = 'FILE_PATH',
        default = tuneloc + "/tune.mp3"
    )

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

    # Checkbox to enable the render cancellation tune play
    cancelTune: bpy.props.BoolProperty(
        name = "Alert Render Cancellation",
        description = "Enable or Disable error tune play when rendering is cancelled",
        default = True)

    # Volume slider control
    tuneVol : bpy.props.FloatProperty(
        name = "Volume",
        description = "Controls the Volume of the tune",
        default = 0.5,
        min = 0.3, soft_max = 1
        )