import cadquery as cq
from cadqueryhelper import parts

hex = parts.make_nonagon()
cq.exporters.export(hex,'out/nonagon.stl')
