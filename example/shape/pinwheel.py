import cadquery as cq
from cadqueryhelper import shape

ring_params = []
ring_params.append({"radius": 150, "start_angle":0})
ring_params.append({"radius":100,"start_angle":30})
ring_params.append({"radius":30,"start_angle":80})

result = shape.pinwheel(
    count = 10, 
    height = 3, 
    ring_params = ring_params
)

#show_object(pattern)
cq.exporters.export(result,'stl/shape_pinwheel.stl')