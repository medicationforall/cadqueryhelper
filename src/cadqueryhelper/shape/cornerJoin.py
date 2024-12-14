# Copyright 2023 James Adams
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

def corner_join(
        length:float = 10, 
        width:float = 6, 
        height:float = 5, 
        side_width:float = 1, 
        corner_chamfer:float = 0
    ) -> cq.Workplane:
    side_a = cq.Workplane("XY").box(length, side_width, height)
    if corner_chamfer:
        side_a = side_a.faces("-X").edges("Y").chamfer(corner_chamfer)
        
    side_b = cq.Workplane("XY").box(side_width, width, height)
    if corner_chamfer:
        side_b = side_b.faces("-Y").edges("X").chamfer(corner_chamfer)
        
    x_translate = (length/2) - (side_width/2)
    y_translate = (width/2) - (side_width/2)
    join = (
        cq.Workplane("XY")
        .union(side_a.translate((0,y_translate,0)))
        .union(side_b.translate((x_translate,0,0)))
    )
    return join