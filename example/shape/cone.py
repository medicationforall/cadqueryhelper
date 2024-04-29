import cadquery as cq
from cadqueryhelper import shape

result = shape.cone(
    radius=1, 
    radius_top=0, 
    height=2
)

#show_object(result)
cq.exporters.export(result,'stl/shape_cone.stl')

