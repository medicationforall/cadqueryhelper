import cadquery as cq
from cadqueryhelper import shape

part = shape.cross(length=10, width=10, height=2, cross_length=1, cross_width=1, x_translate=0, y_translate=0)
cq.exporters.export(part,'out/cross.stl')

if part.metadata:
    print(part.metadata)
