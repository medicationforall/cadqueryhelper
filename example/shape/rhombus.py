import cadquery as cq
from cadqueryhelper import shape

result = shape.rhombus(width=10, offset=4, height=5)
cq.exporters.export(result,'out/rhombus.stl')

if result.metadata:
    print(result.metadata)
