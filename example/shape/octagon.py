import cadquery as cq
from cadqueryhelper import shape

result = shape.regular_polygon(
    radius=10, 
    sides=8
)

#show_object(result)
cq.exporters.export(result,'stl/shape_octagon.stl')
