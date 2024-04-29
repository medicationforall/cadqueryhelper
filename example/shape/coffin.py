import cadquery as cq
from cadqueryhelper import shape

result = shape.coffin(
    length = 30, 
    width = 36,
    height =10,
    top_length = 20,
    base_length = 20, 
    mid_offset = 5
)

#show_object(result)
cq.exporters.export(result,'stl/shape_coffin.stl')