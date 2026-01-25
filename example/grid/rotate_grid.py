import cadquery as cq
from cadqueryhelper.grid import rotate_grid
from cadqueryhelper.shape import arrow

ex_arrow = arrow(
  length=10,
  inner_length=5,
  width=5,
  width_outset=2,
  height=3
)

ex_grid = rotate_grid(
    shape = ex_arrow,
    rotate_increment=-90,
    x_spacing = 10, 
    y_spacing = 10,
    x_count = 4, 
    y_count = 4,
    mod_reset = 4 
)

#show_object(ex_grid)

cq.exporters.export(ex_grid,'stl/grid_rotate.stl')