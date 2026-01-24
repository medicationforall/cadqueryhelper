# Copyright 2025 James Adams
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
from . import triangle_isosceles

def pyramid(
        length:float = 20, 
        width:float = 30, 
        height:float = 25
):
    triangle_one = (
        triangle_isosceles(length=length,width=height, height=width, axis= "XZ")
        .translate((0,width/2,0))
    )
    
    triangle_two = (
        triangle_isosceles(length=width,width=height, height=length, axis= "XZ")
        .translate((0,length/2,0))
        .rotate((0,0,1),(0,0,0),90)
    )
    
    result = (
        cq.Workplane("XY")
        .union(triangle_one)
        .intersect(triangle_two)
    )
    
    return result