import cadquery as cq
from cadqueryhelper import irregular_grid

i_grid = irregular_grid(
    length = 75,
    width = 50,
    height = 2,
    max_height = 10,
    col_size = 5,
    row_size = 5,
    align_z = False,
    include_outline = False,
    passes_count = None,
    seed = "test",
    make_item = None
)

def custom_item(length, width, height):
    return (
        cq.Workplane("XY")
        .box(length-1, width-1, height)
        .chamfer(0.5)
    )

i_grid_2 = irregular_grid(
    length = 150,
    width = 50,
    height = 2,
    max_height = 10,
    col_size = 5,
    row_size = 5,
    align_z = True,
    include_outline = True,
    passes_count = None,
    seed = "test",
    make_item = custom_item
)

i_grid_3_city = irregular_grid(
    length = 100,
    width = 100,
    height = 2,
    col_size = 5,
    row_size = 5,
    max_columns = 4,
    max_rows = 4,
    max_height=10,
    align_z = True,
    include_outline = True,
    union_grid = False,
    passes_count = 400,
    seed = "blue",
    make_item = custom_item
)

i_grid_4_sky_scapers = irregular_grid(
    length = 100,
    width = 100,
    height = 2,
    col_size = 10,
    row_size = 5,
    max_columns = 4,
    max_rows = 4,
    max_height=50,
    align_z = True,
    include_outline = True,
    union_grid = True,
    passes_count = 160,
    seed = "purple",
    make_item = custom_item
)

cq.exporters.export(i_grid, 'stl/grid_irregular.stl')
cq.exporters.export(i_grid_2, 'stl/grid_irregular_2.stl')
cq.exporters.export(i_grid_3_city, 'stl/grid_irregular_3_city.stl')
cq.exporters.export(i_grid_4_sky_scapers, 'stl/grid_irregular_4_sky_scrapers.stl')
