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
from cadqueryhelper import parts

def make_grid(part, dim, odd_col_push = [0,0], columns = 5, rows = 5):
    #print('attempting to make grid');
    grid = cq.Assembly()
    #print('bounds', dir(part.plane))
    for row_i in range(rows):
        row_offset = dim[0] * row_i
        for col_i in range(columns):
            col_offset = dim[1] * col_i

            col_push_x = 0
            col_push_y = 0
            if col_i % 2 == 1:
                col_push_x = odd_col_push[0]
                col_push_y = odd_col_push[1]
            grid.add(part, loc=cq.Location(cq.Vector(row_offset + col_push_x, col_offset + col_push_y, 0)))

    return grid

if __name__ == "__main__":
    #print('this is the grid running as main')
    cube = parts.make_cube(5,5,2)
    cylinder = parts.make_cylinder(2.5,2)
    cone = parts.make_cone()
    grid = make_grid(part=cone, dim = [6,6])
    comp = grid.toCompound()
    cq.exporters.export(comp,'out/grid.stl')
elif __name__ == "temp":
        #log('this is the grid in cq-editor')
        cube = parts.make_cube(5,5,2)
        #cylinder = parts.make_cylinder(2.5,5)

        grid = make_grid(part=cube, dim = [6,6], columns = 8)
        show_object(grid)
