import cadquery as cq
from cadqueryhelper import shape

part = shape.rail(length=6, width=1, height=5, inner_height=1.5)
cq.exporters.export(part,'out/rail.stl')

if part.metadata:
    print(part.metadata)
