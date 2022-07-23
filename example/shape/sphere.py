import cadquery as cq
from cadqueryhelper import parts

part = parts.make_sphere()
cq.exporters.export(part,'out/sphere.stl')

if part.metadata:
    print(part.metadata)
