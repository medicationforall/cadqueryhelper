import cadquery as cq
from cadqueryhelper.grid import grid_points, cell_stretch_points_random

points, stream = grid_points(
    columns = 10,
    rows = 10,
    x_spacing = 5,
    y_spacing = 5
)

example_points = (
    cq.Workplane("XY")
    .pushPoints(stream)
    .box(1,1,1)
)


cell_points = cell_stretch_points_random(
    points,
    x_stretch = (1,3,1),
    y_stretch = (1,3,1),
    seed="chaos",
    uniform_split = True
)

pattern = cq.Workplane("XY")

for points in cell_points:
    face = cq.Workplane("XY").polyline(points).close()
    pattern = pattern.add(face)

show_object(pattern)
show_object(example_points)

print(cell_points)