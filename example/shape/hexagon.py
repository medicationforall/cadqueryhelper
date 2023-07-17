import cadquery as cq
from cadqueryhelper import shape

result = shape.regular_polygon(sides=6)
cq.exporters.export(result,'out/hexagon.stl')

#if part.metadata:
#    print(result.metadata)
