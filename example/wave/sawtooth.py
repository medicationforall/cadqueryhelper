import cadquery as cq
from cadqueryhelper import wave

print('sawtooth test')
result = wave.sawtooth(length=80, width=20, height=3, segment_length=15, inner_width=5)
cq.exporters.export(result,'out/wave_sawtooth.stl')
