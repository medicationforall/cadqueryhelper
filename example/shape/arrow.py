import cadquery as cq
from cadqueryhelper import shape

part = shape.arrow()
cq.exporters.export(part,'out/arrow.stl')

if part.metadata:
    print(part.metadata)
