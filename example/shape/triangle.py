import cadquery as cq
from cadqueryhelper import shape

result = shape.regular_polygon(radius=5, sides=3, height=5)
cq.exporters.export(result,'out/triangle.stl')
