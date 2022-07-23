import cadquery as cq
from cadqueryhelper import shape

part = shape.cone()
cq.exporters.export(part,'out/cone.stl')
