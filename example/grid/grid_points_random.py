import cadquery as cq
from cadqueryhelper.grid import grid_points_random

points, stream = grid_points_random(
    columns = 5,
    rows = 6,
    x_spacing = 10,
    y_spacing = 10,
    shift_x = (-2, 5, 1),#min max step
    shift_y = (-3, 5, .5),#min max step
    seed = 'test'
)

example = cq.Workplane("XY").pushPoints(stream).box(1,1,1)

#show_object(example)
cq.exporters.export(example,'stl/grid_points_random.stl')