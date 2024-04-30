import cadquery as cq
from cadqueryhelper.shape import backdrop

result = backdrop(
    length = 200, 
    width = 250, 
    height = 150,
    thickness = 2,
    operation= 'fillet',#chamfer, fillet
    operation_dist = 20
)

#show_object(result)
cq.exporters.export(result,'stl/shape_backdrop.stl')