import cadquery as cq
from cadqueryhelper import shape

result = shape.pipe()

#show_object(result)
cq.exporters.export(result,'stl/shape_pipe.stl')

