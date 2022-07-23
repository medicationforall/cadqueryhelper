import cadquery as cq
from cadqueryhelper import shape

part = shape.cube()
cq.exporters.export(part,'out/cube.stl')

if part.metadata:
    print(part.metadata)
