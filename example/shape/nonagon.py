import cadquery as cq
from cadqueryhelper import shape

part = shape.regular_polygon(radius=10, sides=9)
cq.exporters.export(part,'out/nonagon.stl')
