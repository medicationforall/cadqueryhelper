import cadquery as cq
from cadqueryhelper import parts

part = parts.make_cylinder()
cq.exporters.export(part,'out/cylinder.stl')

if part.metadata:
    print(part.metadata)
