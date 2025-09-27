import cadquery as cq
from cadqueryhelper import shape

ex_ring = shape.ring(
    diameter = 100,
    inner_diameter = 80,
    height = 4
)

#show_object(ex_ring)
cq.exporters.export(ex_ring,'stl/shape_ring.stl')