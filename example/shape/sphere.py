import cadquery as cq
from cadqueryhelper import shape

part = shape.sphere()
cq.exporters.export(part,'out/sphere.stl')

if part.metadata:
    print(part.metadata)
