import cadquery as cq
from cadqueryhelper import shape

result = shape.chevron(length=10, width=7, height=2, inner_width=3, alt=False)
cq.exporters.export(result,'out/chevron.stl')

alt = shape.chevron(length=10, width=7, height=2, inner_width=3, alt=True)
cq.exporters.export(alt,'out/chevron_alt.stl')
