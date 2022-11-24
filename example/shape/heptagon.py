import cadquery as cq
from cadqueryhelper import shape

result = shape.regular_polygon(radius=10, sides=7)
cq.exporters.export(result,'out/heptagon.stl')
