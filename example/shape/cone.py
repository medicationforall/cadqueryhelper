import cadquery as cq
from cadqueryhelper import parts

part = parts.make_cone()
cq.exporters.export(part,'out/cone.stl')
