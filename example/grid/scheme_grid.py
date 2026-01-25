import cadquery as cq
from cadqueryhelper.grid import scheme_grid
from cadqueryhelper.shape import arrow

ex_arrow = arrow(
  length=10,
  inner_length=5,
  width=5,
  width_outset=2,
  height=3
)

ex_grid = scheme_grid(
    shape = ex_arrow, 
    rotates = [-270,0,-180,-90],
    x_count = 2,
    y_count = 2,
    x_spacing = 10,
    y_spacing = 10,
    x_repeat = 2,
    y_repeat = 2,
)

#show_object(ex_grid)

cq.exporters.export(ex_grid,'stl/grid_scheme.stl')