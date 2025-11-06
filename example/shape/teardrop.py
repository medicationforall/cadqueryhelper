import cadquery as cq
from cadqueryhelper.shape import teardrop

example = teardrop(
    diameter = 5,
    length= 8,
    height = 3
)

#show_object(example)
cq.exporters.export(example,'stl/shape_teardrop.stl')