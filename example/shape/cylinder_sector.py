import cadquery as cq
from cadqueryhelper.shape import cylinder_sector

ex_cylinder = cylinder_sector(
    diameter = 20,  
    angle = 30,
    height = 5
)

#show_object(ex_cylinder)
cq.exporters.export(ex_cylinder,'stl/shape_cylinder_sector.stl')