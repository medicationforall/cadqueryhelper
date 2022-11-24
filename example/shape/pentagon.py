import cadquery as cq
from cadqueryhelper import shape

result = shape.regular_polygon(radius=10, sides=5)
cq.exporters.export(result,'out/pentagon.stl')
