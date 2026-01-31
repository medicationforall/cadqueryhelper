import cadquery as cq
from cadqueryhelper.grid import grid_arc_points_random

points, stream = grid_arc_points_random(
    columns = 10,
    rows = 4,
    x_spacing = 10,
    angle = 90,
    row_increment = 1,
    shift_x = (-10, 10, 1),#min max step
    shift_y = (-10, 10, 1.5),#min max step
    seed= 'tes1'
)

example = cq.Workplane("XY").pushPoints(stream).box(1,1,1)

#show_object(example)
cq.exporters.export(example,'stl/grid_arc_points_random.stl')