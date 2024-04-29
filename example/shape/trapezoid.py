import cadquery as cq
from cadqueryhelper.shape import trapezoid

result = trapezoid(
    length = 75,
    width = 25,
    height = 25,
    top_width = 10
)

#show_object(result)
cq.exporters.export(result,'stl/shape_trapezoid.stl')