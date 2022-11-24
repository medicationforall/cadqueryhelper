import cadquery as cq
from cadqueryhelper import shape

result = shape.cross(length=10, width=10, height=2, cross_length=1, cross_width=1, x_translate=0, y_translate=0)
cq.exporters.export(result,'out/cross.stl')

if result.metadata:
    print(result.metadata)
