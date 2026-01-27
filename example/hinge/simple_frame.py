import cadquery as cq
from cadqueryhelper.hinge import SimpleFrame

bp_frame = SimpleFrame()
bp_frame.length = 30
bp_frame.width = 4
bp_frame.height = 40
bp_frame.frame_width = 1
bp_frame.make()
ex_frame = bp_frame.build()

#show_object(ex_frame)  
cq.exporters.export(ex_frame, 'stl/hinge_simple_frame.stl')