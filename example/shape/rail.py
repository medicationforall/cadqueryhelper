import cadquery as cq
from cadqueryhelper import shape

part = shape.rail()
cq.exporters.export(part,'out/rail.stl')

if part.metadata:
    print(part.metadata)
