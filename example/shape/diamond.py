import cadquery as cq
from cadqueryhelper import shape

part = shape.diamond(length=10, width=5, height=3)
cq.exporters.export(part,'out/diamond.stl')
