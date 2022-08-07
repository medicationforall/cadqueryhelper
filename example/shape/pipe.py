import cadquery as cq
from cadqueryhelper import shape

part = shape.pipe()
cq.exporters.export(part,'out/pipe.stl')

if part.metadata:
    print(part.metadata)
