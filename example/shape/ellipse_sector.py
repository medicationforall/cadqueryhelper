import cadquery as cq
from cadqueryhelper.shape import ellipse_sector

ex_sector = ellipse_sector(
    diameter_x = 20,
    diameter_y = 30,
    angle = 30,
    rotation_angle = 0,
    height = 5,
    debug = True
)

#show_object(ex_sector)
cq.exporters.export(ex_sector, "stl/shape_ellipse_sector.stl")