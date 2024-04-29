import cadquery as cq
from cadqueryhelper import shape

result = shape.star(
    outer_radius=10,
    inner_radius=5,
    points=5,
    height=3
)

#show_object(result)
cq.exporters.export(result,'stl/shape_star.stl')


