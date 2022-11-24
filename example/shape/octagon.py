import cadquery as cq
from cadqueryhelper import shape

result = shape.regular_polygon(radius=10, sides=8)
cq.exporters.export(result,'out/octagon.stl')
