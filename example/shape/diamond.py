import cadquery as cq
from cadqueryhelper import shape

result = shape.diamond(
    length=10, 
    width=5, 
    height=3
)

#show_object(result)
cq.exporters.export(result,'stl/shape_diamond.stl')
