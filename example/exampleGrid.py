import cadquery as cq
from cadqueryhelper import shape
from cadqueryhelper import grid

cube = shape.cube(9,10,2)
cylinder = shape.cylinder(2.5,2)
cone = shape.cone()
hexagon = shape.regular_polygon(sides=6)

ex_grid = grid.make_grid(part=cube, dim = [10,11], rows=7)

#show_object(result)
cq.exporters.export(ex_grid,'stl/grid.stl')
