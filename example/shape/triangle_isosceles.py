import cadquery as cq
from cadqueryhelper.shape import triangle_isosceles

ex_triangle = triangle_isosceles(
    length = 20,
    width = 20, 
    height = 5,
    axis = "XY"
)

#how_object(ex_triangle)
cq.exporters.export(ex_triangle,'stl/shape_triangle_isosceles.stl')