import cadquery as cq
from cadqueryhelper import shape

result = shape.pipe()
cq.exporters.export(result,'out/pipe.stl')

if result.metadata:
    print(result.metadata)
