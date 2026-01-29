import cadquery as cq
from cadqueryhelper.grid import grid_arc_points

points, stream = grid_arc_points(
    columns = 10,
    rows = 8,
    x_spacing = 10,
    angle = 90,
    row_increment = 0
)

example = cq.Workplane("XY").pushPoints(stream).box(1,1,1)

#show_object(example)
cq.exporters.export(example,'stl/grid_arc_points.stl')