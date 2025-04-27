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
from typing import Callable

def scheme_grid(
        shape:cq.Workplane|None = None, 
        rotates:list[float] = [-270,0,-180,-90],
        x_count:int = 2,
        y_count:int = 2,
        x_spacing:float = 10,
        y_spacing:float = 10,
        x_repeat:int = 2,
        y_repeat:int = 2,
    ):
    if not shape:
        raise Exception('Shape can not be None')

    count =0
    def add_rotate(loc:cq.Location) -> cq.Shape:
        nonlocal count
        rotation = rotates[count%len(rotates)]
        
        shape_rotate = shape.rotate((0,0,1),(0,0,0),rotation)
        count+=1
        
        return shape_rotate.val().located(loc) #type:ignore
    
    composite_tile = (
        cq.Workplane("XY")
        .rarray(
            xSpacing = x_spacing, 
            ySpacing = y_spacing,
            xCount = x_count, 
            yCount= y_count, 
            center = True)
        .eachpoint(add_rotate)
    )
    
    composite_union = cq.Workplane("XY").union(composite_tile)
    
    def add_composite(loc:cq.Location) -> cq.Shape:
        return composite_union.val().located(loc) #type:ignore
        
    result = (
        cq.Workplane("XY")
        .rarray(
            xSpacing = x_spacing*x_count, 
            ySpacing = y_spacing*y_count,
            xCount = x_repeat, 
            yCount= y_repeat, 
            center = True)
        .eachpoint(add_composite)
    )
    return result