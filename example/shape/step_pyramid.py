import cadquery as cq
from cadqueryhelper.shape import step_pyramid

example = step_pyramid(
    length = 40,
    width = 60,
    height = 30,
    steps = 3,
    min_length = 10,
    min_width = 15,
    ellipse = False
)

#show_object(example)
cq.exporters.export(example,'stl/shape_step_pyramid.stl')