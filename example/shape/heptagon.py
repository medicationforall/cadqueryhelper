import cadquery as cq
from cadqueryhelper import shape

result = shape.regular_polygon(
    radius=10, 
    sides=7
)

#show_object(result)
cq.exporters.export(result,'stl/shape_heptagon.stl')
