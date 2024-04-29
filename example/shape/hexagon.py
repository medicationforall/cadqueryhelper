import cadquery as cq
from cadqueryhelper import shape

result = shape.regular_polygon(sides=6)

#show_object(result)
cq.exporters.export(result,'stl/shape_hexagon.stl')
