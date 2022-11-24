import cadquery as cq
from cadqueryhelper import shape

result = shape.cylinder(radius=2.5, height=5)
cq.exporters.export(result,'out/cylinder.stl')

if part.metadata:
    print(result.metadata)
