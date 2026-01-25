import cadquery as cq
from cadqueryhelper.grid import randomized_rotation_grid
from cadqueryhelper.shape import arrow

ex_arrow = arrow(
  length=10,
  inner_length=5,
  width=5,
  width_outset=2,
  height=3
)

ex_grid = randomized_rotation_grid(
        shape = ex_arrow, 
        seed = "test",
        rotate_increment = 90, 
        rotate_min = 0, 
        rotate_max = 360,
        x_count = 5,
        y_count = 5,
        x_spacing = 10,
        y_spacing = 10
)

#show_object(ex_grid)

cq.exporters.export(ex_grid,'stl/grid_randomized_rotation.stl')