import cadquery as cq
from cadqueryhelper.grid import grid_points_random

points, stream = grid_points_random(
    columns = 5,
    rows = 6,
    x_spacing = 10,
    y_spacing = 10,
    shift_x = (-2, 5, 1),#min max step
    shift_y = (-3, 5, 1),#min max step
    seed = 'test'
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
cq.exporters.export(example,'stl/grid_points_random_coords.stl')