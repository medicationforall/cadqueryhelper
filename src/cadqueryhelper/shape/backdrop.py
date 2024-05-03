# Copyright 2024 James Adams
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

def backdrop(
        length:float = 200, 
        width:float = 250, 
        height:float = 150,
        thickness:float = 4,
        operation:str = 'fillet',#chamfer, fillet
        operation_dist:float = 20
) -> cq.Workplane:
    box = cq.Workplane('XY').box(length, width, height)
    cut_box = cq.Workplane('XY').box(length, width, height)
    
    if operation == 'chamfer':
        box = box.faces("Y").edges("<Z").chamfer(operation_dist)
        cut_box = cut_box.faces("Y").edges("<Z").chamfer(operation_dist)
    if operation == 'fillet':
        box = box.faces("Y").edges("<Z").fillet(operation_dist)
        cut_box = cut_box.faces("Y").edges("<Z").fillet(operation_dist-thickness)
        
    scene = (
        cq.Workplane("XY")
        .union(box)
        .cut(cut_box.translate((0,-thickness,thickness)))
    )
    return scene