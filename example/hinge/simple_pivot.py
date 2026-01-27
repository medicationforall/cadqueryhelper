import cadquery as cq
from cadqueryhelper.hinge import SimplePivot

bp_pivot = SimplePivot()
bp_pivot.diameter = 4
bp_pivot.height = 43
bp_pivot.make()
ex_pivot= bp_pivot.build()

#show_object(ex_pivot)  
cq.exporters.export(ex_pivot, 'stl/hinge_simple_pivot.stl')