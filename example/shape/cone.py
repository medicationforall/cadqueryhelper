import cadquery as cq
from cadqueryhelper import shape

result = shape.cone(radius=1, radius_top=0, height=2)
cq.exporters.export(result,'out/cone.stl')

if part.metadata:
    print(result.metadata)
