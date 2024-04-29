import cadquery as cq
from cadqueryhelper import shape

result = shape.cube(
    length=5, 
    width=5, 
    height=5
)

#show_object(result)
cq.exporters.export(result,'stl/shape_cube.stl')
