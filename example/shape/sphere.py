import cadquery as cq
from cadqueryhelper import shape

result = shape.sphere(radius=5)
cq.exporters.export(result,'out/sphere.stl')

if part.metadata:
    print(result.metadata)
