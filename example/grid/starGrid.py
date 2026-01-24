import cadquery as cq
from cadqueryhelper import shape
from cadqueryhelper import grid

star = shape.star()

st_grid = grid.make_grid(part = star, dim = [20,20], odd_col_push = [0,0])

#show_object(st_grid)
cq.exporters.export(st_grid,'stl/grid_stargrid.stl')
