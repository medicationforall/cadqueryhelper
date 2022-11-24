import cadquery as cq
from cadqueryhelper import shape

part = shape.star(outer_radius=10, inner_radius=5, points=5, height=3)
cq.exporters.export(part,'out/star.stl')

if part.metadata:
    print(part.metadata)
