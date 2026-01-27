import cadquery as cq
from cadqueryhelper.hinge import SimpleDoor

bp_door = SimpleDoor()
bp_door.length = 30
bp_door.width = 4
bp_door.height = 40
bp_door.rotate_type = 'full'
bp_door.make()
ex_door = bp_door.build()

#show_object(ex_door)
cq.exporters.export(ex_door, 'stl/hinge_simple_door.stl')