import bpy

from .utils.get_mouse_view_coords import get_mouse_frame_and_channel
from .utils.doc import doc_name, doc_idname, doc_brief, doc_description


class DuplicateMove(bpy.types.Operator):
    """
    Auto selects the strip under the mouse if nothing is selected, and calls Blender's
    Duplicate Move function
    """
    doc = {
        'name': doc_name(__qualname__),
        'demo': '',
        'description': doc_description(__doc__),
        'shortcuts': [
            ({'type': 'D', 'value': 'PRESS'}, {}, 'Duplicate Move'),
            ({'type': 'D', 'value': 'PRESS', 'shift': True}, {}, 'Duplicate Move')
        ],
        'keymap': 'Sequencer'
    }
    bl_idname = doc_idname(doc['name'])
    bl_label = doc['name']
    bl_description = doc_brief(doc['description'])
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.sequences

    def invoke(self, context, event):
        frame, channel = get_mouse_frame_and_channel(context, event)
        if not context.selected_sequences:
            bpy.ops.power_sequencer.select_closest_to_mouse(frame=frame,
                                                            channel=channel)
        return self.execute(context)

    def execute(self, context):
        bpy.ops.sequencer.duplicate_move('INVOKE_DEFAULT')
        return {'FINISHED'}

