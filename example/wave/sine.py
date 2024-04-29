import cadquery as cq
from cadqueryhelper import wave

print('sine test')
result = wave.sine(
    length=80,
    width=20,
    height=3,
    segment_length=15,
    inner_width=5
)
#show_object(result)
cq.exporters.export(result,'stl/wave_sine.stl')
