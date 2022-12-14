import cadquery as cq
from cadqueryhelper import shape
from cadqueryhelper import grid

star = shape.star()

st_grid = grid.make_grid(part = star, dim = [20,20], odd_col_push = [0,0])
cq.exporters.export(st_grid,'out/stargrid.stl')
