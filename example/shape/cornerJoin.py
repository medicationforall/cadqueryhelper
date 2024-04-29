import cadquery as cq
from cadqueryhelper import shape

join = shape.corner_join(
    length = 10,
    width = 6,
    height = 5,
    side_width = 1,
    corner_chamfer = 1
)

#show_object(join)
cq.exporters.export(join, 'stl/shape_cornerJoin.stl')