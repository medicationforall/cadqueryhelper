import cadquery as cq
from cadqueryhelper.grid import grid_points_mod, points_randomize

points, stream = grid_points_mod(
    columns = 8,
    rows = 7,
    x_spacing = [5,10],
    y_spacing = 5,
    row_x_mod = [0,1],
    row_x_offset = [0,-2.5]
)

r_points,r_stream = points_randomize(
    points,
    shift_x = (-2,2,.5),
    shift_y = (-2,2,.5),
    seed = 'test'
)

example = cq.Workplane("XY").pushPoints(r_stream).box(1,1,1)

#show_object(example)
cq.exporters.export(example,'stl/grid_points_randomize.stl')