import cadquery as cq
from cadqueryhelper import shape

part = shape.rhombus()
cq.exporters.export(part,'out/rhombus.stl')

if part.metadata:
    print(part.metadata)
