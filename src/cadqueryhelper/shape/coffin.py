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

def coffin(
    length:float = 30, # length between the two mid points
    width:float = 36, # distance between the top and base
    height:float = 10, # extruded height of the face, can be falsy
    top_length:float = 20, # length of the top
    base_length:float = 20, # length of the base
    mid_offset:float = 5 # middle points distance from the width center. Can be positive or negative.
) -> cq.Workplane:
    top_offset = (length - top_length) / 2
    mid_offset = (width/2) + mid_offset
    base_offset = (length - base_length) / 2

    pts = [
        (base_offset,0), # base left
        (length-base_offset,0), # base right 
        (length, mid_offset), # mid right
        (length-top_offset, width), # top right
        (top_offset, width), # top left
        (0, mid_offset) # mid left
    ]

    lines = cq.Workplane("XY").polyline(pts).close()
        
    if height:
        lines = lines.extrude(height).translate((0,0,-1*(height/2)))

    #center along the length and width    
    lines = lines.translate((-1*(length/2),-1*(width/2),0))
        
    return lines