import cadquery as cq
from cadqueryhelper import shape

result = shape.arch_pointed(
    length=30, 
    width=5, 
    height=50, 
    inner_height=25
)

#show_object(result)
cq.exporters.export(result,'stl/shape_arch_pointed.stl')

