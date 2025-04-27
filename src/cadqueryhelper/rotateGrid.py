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

def rotate_grid(
        shape:cq.Workplane|None = None,
        rotate_increment=-90
    ):
    rotation = 0
    count =0

    if not shape:
        raise Exception('rotate_grid: shape can not the None')

    def add_rotate(loc: cq.Location) -> cq.Shape:
        nonlocal rotation
        nonlocal count
        if count% 4 == 0:
            rotation=0
        
        shape_rotate = shape.rotate((0,0,1),(0,0,0),rotation)
        rotation+=rotate_increment
        
        count+=1
    
        return shape_rotate.val().located(loc) #type: ignore
    
    result = (
        cq.Workplane("XY")
        .rarray(
            xSpacing = 10, 
            ySpacing = 10,
            xCount = 4, 
            yCount= 4, 
            center = True)
        .eachpoint(add_rotate)
    )
    return result