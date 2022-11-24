import cadquery as cq
from cadqueryhelper import shape

result = shape.diamond(length=10, width=5, height=3)
cq.exporters.export(result,'out/diamond.stl')
