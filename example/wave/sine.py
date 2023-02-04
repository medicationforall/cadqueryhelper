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
cq.exporters.export(result,'out/wave_sine.stl')
