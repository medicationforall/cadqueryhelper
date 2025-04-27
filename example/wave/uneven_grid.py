import cadquery as cq
from cadqueryhelper.wave import uneven
import random

random.seed('test_3')
def add_uneven(loc:cq.Location)->cq.Shape:
    ex = uneven(
        length = 10, 
        width = 2.5,
        min_width = 0.2,
        step = .5,
        count= (2,8), 
        axis = "XY",
        seed= None,
        offset= 0
    )
    return ex.val().located(loc) #type:ignore

uneven_grid_example = (
    cq.Workplane("XY")
    .rarray(
        xSpacing = 11, 
        ySpacing = 5,
        xCount = 5, 
        yCount= 5, 
        center = True)
    .eachpoint(add_uneven)
).extrude(1)

#show_object(uneven_grid_example)
cq.exporters.export(uneven_grid_example,'stl/wave_uneven_grid.stl')