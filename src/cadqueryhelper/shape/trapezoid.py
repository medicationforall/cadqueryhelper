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

def trapezoid(
        length:float|None = 75, 
        width:float = 25, 
        height:float = 25, 
        top_width:float = 10
    )->cq.Workplane:
    top_x:float = (width - top_width)/2
    
    points = [
        (0,0),
        (top_x,height),
        (top_x+top_width,height),
        (width,0)
    ]

    work = (
        cq.Workplane("XY").center(-(width/2),-(height/2))
        .polyline(points).close()
    )
    
    if length:
        work = work.extrude(length).translate((0,0,-(length/2))).rotate((1,0,0),(0,0,0),-90)
    return work