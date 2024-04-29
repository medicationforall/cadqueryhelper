import cadquery as cq
import math
from cadqueryhelper import wave, shape


pipe_path = cq.Workplane("XZ").spline([(0,0), (20,-20), (50,-20), (50,-30)])

result = shape.star(
    outer_radius=10,
    inner_radius=5,
    points=5,
    height=0
).sweep(pipe_path, multisection = False, isFrenet = False, clean=False)

#show_object(result)
cq.exporters.export(result,'stl/shape_star_sweep.stl')

