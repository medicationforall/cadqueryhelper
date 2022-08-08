import cadquery as cq
from cadqueryhelper import shape

part = shape.regular_polygon(sides=6)
cq.exporters.export(part,'out/hexagon.stl')

if part.metadata:
    print(part.metadata)
