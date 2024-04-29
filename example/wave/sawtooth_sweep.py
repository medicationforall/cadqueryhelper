import cadquery as cq
import math
from cadqueryhelper import wave, shape

length = 20
pipe_path = cq.Workplane("XZ").spline([(0,0), (20,-20), (50,-20), (50,-30)])
result = wave.sawtooth(length, 10, 0, 5, 5).sweep(pipe_path, multisection=False, isFrenet=False, clean=False)


#show_object(result)
cq.exporters.export(result,'stl/wave_sawtooth_sweep.stl')

#show_object(result)
#show_object(pipe_path)
