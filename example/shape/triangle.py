import cadquery as cq
from cadqueryhelper import shape

result = shape.regular_polygon(
    radius=5, 
    sides=3, 
    height=5
)

#show_object(result)
cq.exporters.export(result,'stl/shape_triangle.stl')
