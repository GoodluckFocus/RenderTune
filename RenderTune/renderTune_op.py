import bpy

#TODO Figure out a way to locate the audio track and play
class RENDERTUNE_OT_Operator(bpy.types.Operator):
    bl_idname = "render.rendertuneoperator"
    bl_label = "Render Tune Operator"
    bl_description = "Plays A Tune"
    bl_options = {'REGISTER', 'UNDO'}

    
    
    def execute(self, context):
       



        return {'FINISHED'}