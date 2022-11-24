import cadquery as cq
from cadqueryhelper import shape

result = shape.regular_polygon(radius=10, sides=9)
cq.exporters.export(result,'out/nonagon.stl')
