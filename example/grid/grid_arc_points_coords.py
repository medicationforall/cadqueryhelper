import cadquery as cq
from cadqueryhelper.grid import grid_arc_points

points, stream = grid_arc_points(
    columns = 5,
    rows = 6,
    x_spacing = 10,
    angle = 90,
    row_increment = 0
)

counter = 0
def add_coord_text(loc:cq.Location)->cq.Shape:
    global counter
    coord = loc.toTuple()[0]
    x = coord[0]
    y = coord[1]
    t = cq.Workplane("XY").text(f"{counter}({int(x)},{int(y)})",2.5,1)
    counter += 1
    return t.val().located(loc) #type:ignore

example = (
    cq.Workplane("XY")
    .pushPoints(stream)
    .eachpoint(add_coord_text)
)

#show_object(example)
cq.exporters.export(example,'stl/grid_arc_points_coords.stl')