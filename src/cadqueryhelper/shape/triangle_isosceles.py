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

def triangle_isosceles(
        length:float = 20,
        width:float = 20, 
        height:float = 5,
        axis:str = "XY"
    ):
    pts = [(-length/2,0),(length/2,0),(0,width)]

    triangle_shape = (
        cq.Workplane(axis)
        .polyline(pts)
        .close()
    )
    
    if height:
        triangle_shape = triangle_shape.extrude(height)
    
    return triangle_shape