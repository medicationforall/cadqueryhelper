import cadquery as cq
import math
from cadqueryhelper import wave, shape


#pattern = wave.triangle(length=80, width=20, height=3, segment_length=5, inner_width=5)
#show_object(pattern)

pipe_path = cq.Workplane("XZ").spline([(0,0), (20,-20), (50,-20), (50,-30)])

result = shape.star(
    outer_radius=10,
    inner_radius=5,
    points=5,
    height=0
).sweep(pipe_path, multisection=0, isFrenet=False, clean=False)

cq.exporters.export(result,'out/star_sweep.stl')

#show_object(pipe_path)
#show_object(result)
