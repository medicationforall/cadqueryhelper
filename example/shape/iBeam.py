import cadquery as cq
from cadqueryhelper import shape

result = shape.i_beam(
    length=30,
    width=5,
    height=10,
    web_thickness=2,
    flange_thickness=2,
    join_distance=1.3
)
cq.exporters.export(result,'out/ibeam.stl')
