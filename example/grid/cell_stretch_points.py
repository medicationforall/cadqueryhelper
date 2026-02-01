import cadquery as cq
from cadqueryhelper.grid import grid_points, cell_stretch_points

points, stream = grid_points(
    columns = 10,
    rows = 10,
    x_spacing = 5,
    y_spacing = 5
)

cell_points = cell_stretch_points(
    points,
    x_stretch = 2,
    y_stretch = 2
)

pattern = cq.Workplane("XY")

for points in cell_points:
    face = cq.Workplane("XY").polyline(points).close()
    pattern = pattern.add(face)

#show_object(pattern)