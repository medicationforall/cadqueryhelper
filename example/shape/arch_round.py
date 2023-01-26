import cadquery as cq
from cadqueryhelper import shape

result = shape.arch_round(length=30, width=5, height=50)
cq.exporters.export(result,'out/arch_round.stl')
