import cadquery as cq
from cadqueryhelper.grid import (
    grid_points_mod,
    cell_stretch_points, 
    join_cells_interlock,
    grid_cell_basic
)

points, stream = grid_points_mod(
    columns = 8,
    rows = 7,
    x_spacing = [5,10],
    y_spacing = 5,
    row_x_mod = [0,1],
    row_x_offset = [0,-2.5]
)

cells = cell_stretch_points(
    points,
    x_stretch = 1,
    y_stretch = 1
 )

joined_cells = join_cells_interlock(
        points,
        cells,
        start = 1,
        top_end_index = 3,
        bottom_start_index = 2,
        top_cap_index = 3
)

grid_ex_joined = grid_cell_basic(
    joined_cells,
    height=1,
    taper= 25
)

#show_object(grid_ex_joined)
cq.exporters.export(grid_ex_joined,'stl/grid_joined_cells_interlock.stl')