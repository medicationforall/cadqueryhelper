import cadquery as cq
from cadqueryhelper import shape
from cadqueryhelper import grid

hexagon = shape.regular_polygon(sides=6).rotate((0,0,1),(0,0,0), 30)

ex_grid = grid.make_grid(part = hexagon, dim = [9.5,8], odd_col_push = [4.7,0])

#show_object(result)
cq.exporters.export(ex_grid,'stl/hexgrid.stl')
