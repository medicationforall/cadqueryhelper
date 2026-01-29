import cadquery as cq
from cadqueryhelper.grid import grid_points

points, stream = grid_points(
    columns = 5,
    rows = 6,
    x_spacing = 10,
    y_spacing = 5
)

def add_coord_text(loc:cq.Location)->cq.Shape:
    #log(loc.toTuple())
    coord = loc.toTuple()[0]
    x = coord[0]
    y = coord[1]
    t = cq.Workplane("XY").text(f"({int(x)},{int(y)})",2.5,1)
    return t.val().located(loc) #type:ignore

example = (
    cq.Workplane("XY")
    .pushPoints(stream)
    .eachpoint(add_coord_text)
)

#show_object(example)
cq.exporters.export(example,'stl/grid_points_coords.stl')