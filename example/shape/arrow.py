import cadquery as cq
from cadqueryhelper import shape

part = shape.arrow(length=10, inner_length=5, width=5, width_outset=2, height=3)
cq.exporters.export(part,'out/arrow.stl')

if part.metadata:
    print(part.metadata)
