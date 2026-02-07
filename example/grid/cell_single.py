import cadquery as cq
from cadqueryhelper.grid import cell_single

points:list[tuple[float,float]] = [
    (0,0),
    (0,4),
    (4,4),
    (4,0)
]

ex_cell = cell_single(
    points=points,
    height=1,
    taper=25,
    offset=-.25
)

#show_object(ex_cell)
cq.exporters.export(ex_cell,'stl/grid_cell_single.stl')