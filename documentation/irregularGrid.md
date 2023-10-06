# Irregular Grid Documentation

## Irregular Grid
### Parameters
* **length** = 75 - Length of the grid.
* **width** = 50 - Width of the Grid.
* **height** = 2 - Initial height of the Grid items.
* **col_size** = 5 - Length of the column divisions.
* **row_size** = 5 - Width of the row divisions.
* **max_columns** = None - Each item can span a max of N columns.
* **max_rows** = None - Each item can span a max of N rows.
* **max_height** = 2 - Randomly rolled max height of items.
* **align_z** = False - When True centers each item on the z axis.
* **include_outline** = False - Render baseplate solid, helpful for debugging.
* **union_grid** = True - Add items to the grid using union command, otherwise uses add command.
* **passes_count** = None - Max number of render passes, None means run until the grid is full.
* **seed** = "test" - Pseudo random item placement is effected by this string, change this to get different output results.
* **make_item** = None - Callback method for making items. Whatever method you feed this has to accept three parameters length, width, and height. The passed in method should return a workplane with a solid.
* **fill_cells** = None - Allows you to hardcode items to specific start points and dimensions. 

### An Uninteresting Grid
![](image/irregularGrid/05.png)<br />

``` python
import cadquery as cq
from cadqueryhelper import irregular_grid

grid = irregular_grid(
    length = 75,
    width = 50,
    height = 2,
    max_height = 2,
    max_columns = 1,
    max_rows = 1,
    col_size = 5,
    row_size = 5,
    align_z = False,
    include_outline = False,
    passes_count = None,
    seed = "test",
    make_item = None,
    union_grid = False,
)
```

### Example
``` python
def custom_item(length, width, height):
    return (
        cq.Workplane("XY")
        .box(length-1, width-1, height)
        .chamfer(0.5)
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
```

![](image/irregularGrid/04.png)<br />
