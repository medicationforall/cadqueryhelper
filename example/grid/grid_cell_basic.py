import cadquery as cq
from cadqueryhelper.grid import grid_points, cell_stretch_points, grid_cell_basic

points, stream = grid_points(
    columns = 10,
    rows = 10,
    x_spacing = 5,
    y_spacing = 5
)

cell_points = cell_stretch_points(
    points,
    x_stretch = 3,
    y_stretch = 3
)

grid = grid_cell_basic(
    cell_points,
    height=1,
    taper= 25
)

#show_object(grid)
cq.exporters.export(grid,'stl/grid_cell_basic.stl')