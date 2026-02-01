import cadquery as cq
from cadqueryhelper.grid import grid_arc_points, cell_stretch_points, grid_cell_basic

points, stream = grid_arc_points(
    columns = 13,
    rows = 13,
    x_spacing = 5,
    angle = 180
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
cq.exporters.export(grid,'stl/grid_cell_basic_arc.stl')