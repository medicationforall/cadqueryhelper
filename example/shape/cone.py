import cadquery as cq
from cadqueryhelper import shape

part = shape.cone(radius=1, radius_top=0, height=2)
cq.exporters.export(part,'out/cone.stl')

if part.metadata:
    print(part.metadata)
