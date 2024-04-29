import cadquery as cq
import math
from cadqueryhelper import wave, shape


pipe_path = cq.Workplane("XZ").spline([(0,0), (20,-20), (50,-20), (50,-30)])
comb = result = wave.square(
    length=70,
    width=10,
    height=10,
    segment_length=20,
    inner_width=5
).translate((0,35,0))

comb2 = result = wave.sawtooth(
    length=70,
    width=10,
    height=10,
    segment_length=20,
    inner_width=5
).translate((0,35,0))

comb3 = result = wave.triangle(
    length=70,
    width=10,
    height=10,
    segment_length=10,
    inner_width=4
).translate((0,35,0))

comb4 = result = wave.sine(
    length=70,
    width=10,
    height=10,
    segment_length=10,
    inner_width=5
).translate((0,35,0))

composite = (
    cq.Workplane("XY")
    .union(comb)
    .union(comb2.rotate((0,0,1),(0,0,0),90))
    .union(comb3.rotate((0,0,1),(0,0,0),180))
    .union(comb4.rotate((0,0,1),(0,0,0),270))
    .translate((0,0,-5))
    .faces("Z").wires().toPending().twistExtrude(100,180, combine=False)
)

#show_object(composite)
cq.exporters.export(composite,'stl/wave_square_twist_extrude2.stl')
