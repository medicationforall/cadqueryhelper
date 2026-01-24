import cadquery as cq
from cadqueryhelper.hinge import Hinge

bp = Hinge()

bp.length = 100
bp.radius = 4
bp.segments = 10 
bp.pad = 1

bp.base_inset = 0.6
bp.key_length = 1.5
bp.key_width = 0.5

bp.tab_length = 10
bp.tab_height = 8
bp.tab_z_translate = 4
bp.rotate_deg = 0 #90
bp.plate_spacer = 0.4

bp.render = "both"
bp.make()

hinge_test = bp.build()
scene = cq.Workplane("XY").union(hinge_test)

bp.render = "driver"
bp.make()
hinge_driver = bp.build()
scene = scene.add(hinge_driver.translate((0,50,0)))

bp.render = "receiver"
bp.make()
hinge_receiver = bp.build()
scene = scene.add(hinge_receiver.translate((0,30,0)))


#show_object(scene)
cq.exporters.export(scene, 'stl/hinge_render.stl')