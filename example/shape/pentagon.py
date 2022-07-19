import cadquery as cq
from cadqueryhelper import parts

hex = parts.make_pentagon()
cq.exporters.export(hex,'out/pentagon.stl')
