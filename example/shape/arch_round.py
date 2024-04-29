import cadquery as cq
from cadqueryhelper import shape

result = shape.arch_round(
    length=30, 
    width=5, 
    height=50
)

#show_object(result)
cq.exporters.export(result,'stl/shape_arch_round.stl')
