import cadquery as cq
from cadqueryhelper import parts

hex = parts.make_hexagon()
cq.exporters.export(hex,'out/hexagon.stl')
