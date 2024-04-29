import cadquery as cq
from cadqueryhelper import shape

result = shape.rhombus(
    width=10, 
    offset=4, 
    height=5
)

#show_object(result)
cq.exporters.export(result,'stl/shape_rhombus.stl')

