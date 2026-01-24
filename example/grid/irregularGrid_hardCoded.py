import cadquery as cq
from cadqueryhelper.grid import irregular_grid

ig = irregular_grid(
    length = 100,
    width = 50,
    col_size = 10,
    row_size = 10,
    union_grid=False,
    seed="test3",
    fill_cells = [(0,0,4,3), (4,0,2,4)],
    passes_count=None
)

#show_object(ig)
cq.exporters.export(ig, 'stl/grid_irregular_hardcoded.stl')
