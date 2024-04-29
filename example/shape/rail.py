import cadquery as cq
from cadqueryhelper import shape

result = shape.rail(
    length=6, 
    width=1, 
    height=5, 
    inner_height=1.5
)

#show_object(result)
cq.exporters.export(result,'stl/shape_rail.stl')
