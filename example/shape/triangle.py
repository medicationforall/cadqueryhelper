import cadquery as cq
from cadqueryhelper import shape

part = shape.regular_polygon(radius=5, sides=3)
cq.exporters.export(part,'out/triangle.stl')
