import cadquery as cq
from cadqueryhelper import parts

hex = parts.make_octagon()
cq.exporters.export(hex,'out/octagon.stl')
