import cadquery as cq
from cadqueryhelper import shape

result = shape.lightning(
    length = 25,
    width = 50,
    height = 5,
    x_dist = 3,
    y_dist = 6
)

#show_object(result)
cq.exporters.export(result,'stl/shape_lightning.stl')
