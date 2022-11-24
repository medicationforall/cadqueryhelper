import cadquery as cq
from cadqueryhelper import shape

result = shape.arch_pointed(length=30, width=5, height=50, inner_height=25)
cq.exporters.export(result,'out/arch_pointed.stl')

if result.metadata:
    print(result.metadata)
