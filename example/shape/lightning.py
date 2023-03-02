import cadquery as cq
from cadqueryhelper import shape

result = shape.lightning(
    length = 25,
    width = 50,
    height = 5,
    x_dist = 3,
    y_dist = 6
)

cq.exporters.export(result,'out/lightning.stl')
