import cadquery as cq
from cadqueryhelper import shape

part = shape.regular_polygon(radius=10, sides=7)
cq.exporters.export(part,'out/heptagon.stl')
