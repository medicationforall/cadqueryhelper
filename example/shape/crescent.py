import cadquery as cq
from cadqueryhelper.shape import crescent 

ex_crescent = crescent(
    diameter = 30, 
    shift = 10,
    height = 5
)

#show_object(ex_crescent)
cq.exporters.export(ex_crescent,'stl/shape_crescent.stl')