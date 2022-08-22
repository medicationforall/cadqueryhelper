import cadquery as cq
from cadqueryhelper import shape

part = shape.arch_pointed(length=30, width=5, height=50, inner_height=25, inner_width=3)
cq.exporters.export(part,'out/arch_pointed.stl')

if part.metadata:
    print(part.metadata)
