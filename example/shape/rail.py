import cadquery as cq
from cadqueryhelper import shape

result = shape.rail(length=6, width=1, height=5, inner_height=1.5)
cq.exporters.export(result,'out/rail.stl')

if result.metadata:
    print(result.metadata)
