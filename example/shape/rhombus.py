import cadquery as cq
from cadqueryhelper import parts

hex = parts.make_rhombus()
cq.exporters.export(hex,'out/rhombus.stl')
