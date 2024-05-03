import cadquery as cq
from cadqueryhelper.shape import jersey_barrier

result = jersey_barrier(
    length=75,
    width = 20,
    height = 25,
    base_height = 4,
    middle_width_inset = -4,
    middle_height = 2,
    top_width_inset = -1
)

#show_object(j_barrier_ex)
cq.exporters.export(result,'stl/shape_jersey_barrier.stl')