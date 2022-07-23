import cadquery as cq
from cadqueryhelper import shape

part = shape.star()
cq.exporters.export(part,'out/star.stl')

if part.metadata:
    print(part.metadata)
