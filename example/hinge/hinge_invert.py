import cadquery as cq
from cadqueryhelper.hinge import Hinge

bp_hinge = Hinge()
bp_hinge.segments = 3
bp_hinge.rotate_deg = -30
bp_hinge.make()
hinge = bp_hinge.build()

bp_hinge_two = Hinge()
bp_hinge_two.segments = 3
bp_hinge_two.rotate_deg = -30
bp_hinge_two.invert = True
bp_hinge_two.make()
hinge_invert = bp_hinge_two.build()



scene = (
    cq.Workplane("XY")
    .add(hinge)
    .add(hinge_invert.translate((0,30,0)))
    
)

#show_object(scene)
cq.exporters.export(scene, 'stl/hinge_invert.stl')