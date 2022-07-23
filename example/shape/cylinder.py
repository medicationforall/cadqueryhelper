import cadquery as cq
from cadqueryhelper import shape

part = shape.cylinder()
cq.exporters.export(part,'out/cylinder.stl')

if part.metadata:
    print(part.metadata)
