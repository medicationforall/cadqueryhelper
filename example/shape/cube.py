import cadquery as cq
from cadqueryhelper import shape

part = shape.cube(length=5, width=5, height=5)
cq.exporters.export(part,'out/cube.stl')

if part.metadata:
    print(part.metadata)
