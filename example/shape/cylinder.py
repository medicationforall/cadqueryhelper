import cadquery as cq
from cadqueryhelper import shape

result = shape.cylinder(
    radius=2.5, 
    height=5
)

#show_object(result)
cq.exporters.export(result,'stl/shape_cylinder.stl')
