import cadquery as cq
from cadqueryhelper import shape

part = shape.cylinder(radius=2.5, height=5)
cq.exporters.export(part,'out/cylinder.stl')

if part.metadata:
    print(part.metadata)
