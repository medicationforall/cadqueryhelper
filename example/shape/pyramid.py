import cadquery as cq
from cadqueryhelper.shape import pyramid

ex_pyramid = pyramid(
    length = 20, 
    width = 30, 
    height = 25
)

#show_object(ex_pyramid)
cq.exporters.export(ex_pyramid,'stl/shape_pyramid.stl')