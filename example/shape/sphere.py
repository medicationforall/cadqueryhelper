import cadquery as cq
from cadqueryhelper import shape

result = shape.sphere(
    radius=5
)

#show_object(result)
cq.exporters.export(result,'stl/shape_sphere.stl')

