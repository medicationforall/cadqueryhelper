# Copyright 2022 James Adams
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import cadquery as cq
import math
import random

def custom_item(length, width, height):
    log('custom item')
    return (
        cq.Workplane("XY")
        .box(length-1, width-1, height)
        .chamfer(0.5)
    )

def irregular_grid(
        length = 75,
        width = 50,
        height = 2,
        col_size = 5,
        row_size = 5,
        max_columns = None,
        max_rows = None,
        max_height = 2,
        align_z = False,
        include_outline = False,
        union_grid = True,
        passes_count = None,
        seed = "test",
        make_item = None
    ):
    #log('** make irregular_grid **')
    random.seed(seed)
    columns = math.floor(length/col_size)
    rows = math.floor(width / row_size)
    bool_grid = boolean_matrix(columns, rows)
    position = [(0,0)]
    outline = cq.Workplane("XY").box(length, width, height)

    grid = (cq.Workplane("XY"))

    if include_outline:
        grid = grid.union(outline)

    if not max_columns:
        max_columns = columns


    if not max_rows:
        max_rows = rows

    while passes_count == None or len(position) <= passes_count:
        item_length = random.randrange(col_size,(max_columns+1)*col_size, col_size)
        item_width = random.randrange(row_size,(max_rows+1)*row_size, row_size)

        if height == max_height or max_height == None:
            item_height = height
        else:
            item_height = random.randrange(height, max_height)

        if __will_item_fit(
                bool_grid,
                position[-1],
                int(item_length/col_size),
                int(item_width/row_size),
                columns,
                rows
            ):
            grid = __add_item(
                bool_grid,
                grid,
                length,
                width,
                item_length,
                item_width,
                item_height,
                col_size,
                row_size,
                position,
                align_z,
                union_grid,
                make_item
            )
            next_position = __find_next_start_position(bool_grid)
            if next_position:
                position.append(next_position)
            else:
                #log(f'Done! {len(position)}')
                break
        else:
            position.append(position[-1])
    return grid

def __will_item_fit(
        bool_grid,
        position,
        length,
        width,
        columns,
        rows
        ):

    if position[0]+length >columns:
        fit = False
        #log(f'item is too long {position[0]+length} > {columns}')
        return False

    if position[1]+width > rows:
        fit = False
        #log(f'item is too wide {position[1]+width} > {rows}')
        return False

    for row in range(position[1],position[1]+width):
        for col in range(position[0],position[0]+length):
            cell = bool_grid[row][col]
            if not cell:
                #log(f'it doesn\'t fit {col},{row} - {position}')
                return  False
    #log(f'item will fit {length}*{width} fit at position {position}')
    return True

def __add_item(
        bool_grid,
        grid,
        length,
        width,
        item_length,
        item_width,
        item_height,
        col_size,
        row_size,
        position,
        align_z = False,
        union_grid = True,
        make_item = None
    ):

    if make_item:
        item = make_item(item_length, item_width, item_height)
    else:
        item = __make_item(item_length, item_width, item_height)

    x_translate= -1*(length/2-item_length/2)
    x_translate += position[-1][0]*col_size

    y_translate = (width/2-item_width/2)
    y_translate += -1*(position[-1][1]*row_size)

    z_translate = 2* len(position)
    z_translate = 0

    if align_z:
        z_translate = item_height/2

    if union_grid:
        grid = grid.union(item.translate((
            x_translate,
            y_translate,
            z_translate
        )))
    else:
        grid = grid.add(item.translate((
            x_translate,
            y_translate,
            z_translate
        )))
    __mark_item_to_bool(
        bool_grid,
        position[-1],
        int(item_length/col_size),
        int(item_width/row_size
    ))

    return grid
    #print(bool_grid)

def __mark_item_to_bool(bool_grid, position, x, y):
    #log(f'__mark_item_to_bool {position}, {x}, {y}')

    for row in range(position[1],position[1]+y):
        for col in range(position[0],position[0]+x):
            bool_grid[row][col]=False

def __find_next_start_position(bool_grid):
    #log('__find_next_start_position')
    for ri,row in enumerate(bool_grid):
        for ci, col in enumerate(row):
            if col:
                #log(f'next start position is ({ci},{ri})')
                return (ci, ri)
    return None

def __make_item(length, width, height=2):
    item = cq.Workplane("XY").box(length, width, height)
    return item

def boolean_matrix(columns=10, rows=10):
    matrix = []
    for r in range(rows):
        row = []
        for c in range(columns):
            row.append(True)
        matrix.append(row)
    return matrix
