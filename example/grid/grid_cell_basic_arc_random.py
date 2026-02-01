import cadquery as cq
from cadqueryhelper.grid import grid_arc_points_random, cell_stretch_points, grid_cell_basic

points, stream = grid_arc_points_random(
    columns = 17,
    rows = 6,
    x_spacing = 5,
    angle = 90,
    shift_x = (-2, 2, 1),#min max step
    shift_y = (-3, 2, .5),#min max step
    seed = 'test'
)

cell_points = cell_stretch_points(
    points,
    x_stretch = 2,
    y_stretch = 4
)

grid = grid_cell_basic(
    cell_points,
    height=1,
    taper= 30
)

#show_object(grid)
cq.exporters.export(grid,'stl/grid_cell_basic_arc_random.stl')