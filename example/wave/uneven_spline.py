import cadquery as cq
from cadqueryhelper.wave import uneven_spline

result = uneven_spline(
    length = 10, 
    width = 2.5,
    min_width = 0.5,
    step = .5,
    count = (2,8), 
    axis = "XY",
    seed = "test",
    offset = 0
)

#show_object(result)

cq.exporters.export(result.extrude(1),'stl/wave_uneven_spline.stl')