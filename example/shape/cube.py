import cadquery as cq
from cadqueryhelper import parts

part = parts.make_cube()
cq.exporters.export(part,'out/cube.stl')

if part.metadata:
    print(part.metadata)
