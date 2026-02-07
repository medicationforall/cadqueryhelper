import cadquery as cq
from cadqueryhelper.grid import grid_points, cell_stretch_points, grid_cell_random

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

grid = grid_cell_random(
    cell_points,
    height = (1,5,1),
    offset = (-1,0,.25),
    taper = (5,60,5),
    seed = 'abhi'
)

#show_object(grid)
cq.exporters.export(grid,'stl/grid_cell_random.stl')