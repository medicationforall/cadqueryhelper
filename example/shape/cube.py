import cadquery as cq
from cadqueryhelper import shape

result = shape.cube(length=5, width=5, height=5)
cq.exporters.export(result,'out/cube.stl')

if part.metadata:
    print(result.metadata)
