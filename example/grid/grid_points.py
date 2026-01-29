import cadquery as cq
from cadqueryhelper.grid import grid_points

points, stream = grid_points(
    columns = 5,
    rows = 6,
    x_spacing = 5,
    y_spacing = 5
)
example = cq.Workplane("XY").pushPoints(stream).box(1,1,1)

#show_object(example)
cq.exporters.export(example,'stl/grid_points.stl')