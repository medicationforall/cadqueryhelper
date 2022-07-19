import cadquery as cq
from cadqueryhelper import parts

part = parts.make_heptagon()
cq.exporters.export(part,'out/heptagon.stl')
