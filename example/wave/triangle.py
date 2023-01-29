import cadquery as cq
from cadqueryhelper import wave

result = wave.triangle(
    length=80,
    width=20,
    height=3,
    segment_length=5,
    inner_width=5
)
cq.exporters.export(result,'out/wave_triangle.stl')
