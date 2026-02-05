import cadquery as cq
from cadqueryhelper.grid import grid_points_mod ,cell_stretch_points, grid_cell_basic

points, stream = grid_points_mod(
    columns = 10,
    rows = 10,
    x_spacing = [5,10],
    y_spacing = [5],
    row_x_mod = [0,1],
    row_x_offset = [0,-2.5]
)

cell_points = cell_stretch_points(
    points,
    x_stretch = 1,
    y_stretch = 1
)

grid = grid_cell_basic(
    cell_points,
    height=1,
    taper= 25
)

#show_object(grid)
cq.exporters.export(grid,'stl/grid_cell_basic_mod.stl')