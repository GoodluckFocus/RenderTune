import bpy

class RENDERTUNE_OT_Operator(bpy.types.Operator):
    bl_idname = "render.rendertuneoperator"
    bl_label = "Render Tune Operator"
    bl_description = "Plays Audio"


    def execute(self, context):
        #TODO create a way to retrieve tune to be played/ library audio

        return {'FINISHED'}