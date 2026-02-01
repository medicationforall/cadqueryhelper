import cadquery as cq
from cadqueryhelper.grid import grid_points_random, cell_stretch_points, grid_cell_basic

points, stream = grid_points_random(
    columns = 10,
    rows = 10,
    x_spacing = 5,
    y_spacing = 5,
    shift_x = (-2, 2, 1),#min max step
    shift_y = (-2, 2, .5),#min max step
    seed = 'test9'
)

cell_points = cell_stretch_points(
    points,
    x_stretch = 3,
    y_stretch = 2
)

grid = grid_cell_basic(
    cell_points,
    height=1,
    taper= 15
)

#show_object(grid)
cq.exporters.export(grid,'stl/grid_cell_basic_random.stl')