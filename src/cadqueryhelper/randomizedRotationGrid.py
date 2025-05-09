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
import random
from typing import Callable

def randomized_rotation_grid(
        shape:cq.Workplane|None = None, 
        seed:str|None = "test",
        rotate_increment:int = 90, 
        rotate_min:int = 0, 
        rotate_max:int = 360,
        x_count:int = 5,
        y_count:int = 5,
        x_spacing:float = 10,
        y_spacing:float = 10
    ) -> cq.Workplane:

    if seed:
        random.seed(seed)

    if not shape:
        raise Exception("Missing shape")
    
    def add_rotate(loc:cq.Location) -> cq.Shape:
        rotation = random.randrange(rotate_min, rotate_max, rotate_increment)
        shape_rotate = shape.rotate((0,0,1),(0,0,0),rotation)
        return shape_rotate.val().located(loc) #type:ignore
    
    result = (
        cq.Workplane("XY")
        .rarray(
            xSpacing = x_spacing, 
            ySpacing = y_spacing,
            xCount = x_count, 
            yCount= y_count, 
            center = True)
        .eachpoint(add_rotate)
    )
    return result