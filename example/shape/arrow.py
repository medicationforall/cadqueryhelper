import cadquery as cq
from cadqueryhelper import shape

result = shape.arrow(length=10, inner_length=5, width=5, width_outset=2, height=3)
cq.exporters.export(result,'out/arrow.stl')

if result.metadata:
    print(result.metadata)
