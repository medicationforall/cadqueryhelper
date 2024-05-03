import cadquery as cq
from cadqueryhelper.shape import vase
from cadqueryhelper.wave import sine

test_shape = cq.Workplane("XY").rect(4,8)
result = vase(
    test_shape, 
    workplane_axis = "YZ",
    radius = 10, 
    angle=0, 
    rotation_angle=0
)

#show_object(result)
cq.exporters.export(result,'stl/shape_vase_basic.stl')

#--------------------

shape_wave = sine(
    length=80,
    width=20,
    height=0,
    segment_length=15,
    inner_width=5
)

result2 = vase(
    shape_wave, 
    workplane_axis = "YZ",
    radius = 10, 
    angle=0, 
    rotation_angle=0
)

#show_object(result)
cq.exporters.export(result2,'stl/shape_vase_ripple.stl')

#--------------------

shape_wave_2 = sine(
    length=80,
    width=20,
    height=0,
    segment_length=15,
    inner_width=5
)

result3 = vase(
    shape_wave_2,
    workplane_axis = "XZ",
    radius = 10, 
    angle=0, 
    rotation_angle=0
)
cq.exporters.export(result3,'stl/shape_vase.stl')