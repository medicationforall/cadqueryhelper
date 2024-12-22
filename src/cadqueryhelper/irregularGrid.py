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
from typing import Callable

def custom_item(
        length:float, 
        width:float, 
        height:float
    ) -> cq.Workplane:
    return (
        cq.Workplane("XY")
        .box(length-1, width-1, height)
        .chamfer(0.5)
    )

def irregular_grid(
        length:float = 75,
        width:float = 50,
        height:float = 2,
        col_size:float = 5,
        row_size:float = 5,
        max_columns:int|None = None,
        max_rows:int|None = None,
        max_height:float = 2,
        align_z:bool = False,
        include_outline:bool = False,
        union_grid:bool = True,
        passes_count:int|None = None,
        seed:str|None = "test",
        make_item:Callable[[float, float, float], cq.Workplane]|None = None,
        fill_cells:list|None = None
    ) -> cq.Workplane:
    #log('** make irregular_grid **')

    if seed:
        random.seed(seed)
        
    columns = math.floor(length/col_size)
    rows = math.floor(width / row_size)
    bool_grid = __boolean_matrix(columns, rows)
    outline = cq.Workplane("XY").box(length, width, height)
    grid = (cq.Workplane("XY"))

    if include_outline:
        grid = grid.union(outline)

    if not max_columns:
        max_columns = columns

    if not max_rows:
        max_rows = rows

    position:list = [__find_next_start_position(bool_grid)]

    if fill_cells and len(fill_cells) > 0:
        for fill in fill_cells:
            position.append((fill[0], fill[1]))
            item_length = fill[2]*col_size
            item_width = fill[3]*row_size

            if height == max_height or max_height == None:
                item_height = height
            else:
                item_height = random.uniform(height, max_height)

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

    while passes_count == None or len(position) <= passes_count:
        item_length = random.randrange(int(col_size),int((max_columns+1)*col_size), int(col_size))
        item_width = random.randrange(int(row_size),int((max_rows+1)*row_size), int(row_size))

        if height == max_height or max_height == None:
            item_height = height
        else:
            item_height = random.uniform(height, max_height)

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
        bool_grid:list[list[bool]],
        position:tuple[int,int],
        length:float,
        width:float,
        columns:int,
        rows:int
        ):

    if position[0]+length >columns:
        fit = False
        #log(f'item is too long {position[0]+length} > {columns}')
        return False

    if position[1]+width > rows:
        fit = False
        #log(f'item is too wide {position[1]+width} > {rows}')
        return False

    for row in range(position[1],int(position[1]+width)):
        for col in range(position[0],int(position[0]+length)):
            cell = bool_grid[row][col]
            if not cell:
                #log(f'it doesn\'t fit {col},{row} - {position}')
                return  False
    #log(f'item will fit {length}*{width} fit at position {position}')
    return True

def __add_item(
        bool_grid:list[list[bool]],
        grid:cq.Workplane,
        length:float,
        width:float,
        item_length:float,
        item_width:float,
        item_height:float,
        col_size:float,
        row_size:float,
        position:list[tuple[int,int]],
        align_z:bool = False,
        union_grid:bool = True,
        make_item:Callable[[float, float, float], cq.Workplane]|None = None
    ) -> cq.Workplane:

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

def __mark_item_to_bool(
        bool_grid:list[list[bool]], #pass by reference
        position:tuple[int,int], 
        x:int, 
        y:int
    ) -> None:
    #log(f'__mark_item_to_bool {position}, {x}, {y}')

    for row in range(position[1],position[1]+y):
        for col in range(position[0],position[0]+x):
            bool_grid[row][col]=False

def __find_next_start_position(
        bool_grid:list[list[bool]]
    ) -> tuple[int,int]|None:
    #log('__find_next_start_position')
    for ri,row in enumerate(bool_grid):
        for ci, col in enumerate(row):
            if col:
                #log(f'next start position is ({ci},{ri})')
                return (ci, ri)
    return None

def __make_item(
        length:float, 
        width:float, 
        height:float = 2
    ) -> cq.Workplane:
    item = cq.Workplane("XY").box(length, width, height)
    return item

def __boolean_matrix(
        columns:int = 10, 
        rows:int = 10
    ) -> list[list[bool]]:
    matrix = []
    for r in range(rows):
        row = []
        for c in range(columns):
            row.append(True)
        matrix.append(row)
    return matrix
