import cadquery as cq
from cadqueryhelper.hinge import SimpleHinge

bp_hinge = SimpleHinge()
bp_hinge.length = 40
bp_hinge.width = 4
bp_hinge.height = 42
bp_hinge.margin = 0.4
bp_hinge.frame_width = 2
bp_hinge.pivot_diameter = 3
bp_hinge.pivot_height = bp_hinge.height - 1.5
bp_hinge.door_width = None
bp_hinge.rotate = 0
bp_hinge.rotate_type = "full"
bp_hinge.make()
ex_hinge = bp_hinge.build()

#show_object(ex_hinge)
cq.exporters.export(ex_hinge, 'stl/hinge_simple_hinge.stl')