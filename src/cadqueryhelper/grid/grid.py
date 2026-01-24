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

def make_grid(
        part:cq.Workplane, 
        dim:list, 
        odd_col_push:list[float] = [0,0], 
        columns:int = 5, 
        rows:int = 5
    ) -> cq.Workplane:
    grid = cq.Assembly()
    for row_i in range(rows):
        row_offset = (dim[0] * row_i)
        for col_i in range(columns):
            col_offset = (dim[1] * col_i)

            col_push_x = 0
            col_push_y = 0
            if col_i % 2 == 1:
                col_push_x = odd_col_push[0]
                col_push_y = odd_col_push[1]
            grid.add(part, loc=cq.Location(cq.Vector(row_offset + col_push_x, col_offset + col_push_y, 0)))

    length = dim[1] * columns
    width = dim[0] * rows

    comp = grid.toCompound()
    work = cq.Workplane("XZ").center(0, 0).workplane()
    work.add(comp)

    # zero out the grid
    work = work.translate(((dim[0]/2),(dim[1]/2)))
    work = work.translate((-1*(width/2),-1*(length/2)))

    return work
