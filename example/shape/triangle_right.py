import cadquery as cq
from cadqueryhelper.shape import triangle_right

ex_triangle = triangle_right(
    length = 50, 
    width = 40, 
    height= 5
)

#show_object(ex_triangle)
cq.exporters.export(ex_triangle,'stl/shape_triangle_right.stl')