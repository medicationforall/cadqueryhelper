import cadquery as cq
from cadqueryhelper import parts

part = parts.make_triangle()
cq.exporters.export(part,'out/triangle.stl')
