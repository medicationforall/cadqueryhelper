import cadquery as cq
from cadqueryhelper import pattern

result = pattern.triangle(length=80, width=20, height=3, segment_length=5, inner_width=5)
cq.exporters.export(result,'out/pattern_triangle.stl')
