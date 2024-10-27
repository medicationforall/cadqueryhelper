import cadquery as cq
from cadqueryhelper.wave import uneven

result = uneven(
    length = 10, 
    width = 2.5,
    min_width = 0.0001,
    step = .5,
    count = (2,8), 
    axis = "XY",
    seed = "test",
    offset = 0
)

cq.exporters.export(result.extrude(1),'stl/wave_uneven.stl')
