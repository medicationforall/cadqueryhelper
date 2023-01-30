import cadquery as cq
from cadqueryhelper import wave

print('square test')
result = wave.square(
    length=75.5,
    width=10,
    height=3,
    segment_length=5,
    inner_width=5
)

cq.exporters.export(result,'out/wave_square.stl')
