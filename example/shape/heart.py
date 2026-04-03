import cadquery as cq
from cadqueryhelper import shape

result = shape.heart(
    diameter = 15,
    length = 15,
    height = 3
)

#show_object(result)
cq.exporters.export(result,'stl/shape_heart.stl')