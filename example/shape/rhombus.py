import cadquery as cq
from cadqueryhelper import shape

part = shape.rhombus(width=10, offset=4, height=5)
cq.exporters.export(part,'out/rhombus.stl')

if part.metadata:
    print(part.metadata)
