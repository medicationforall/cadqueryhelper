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

def cross(
        length:float = 10, 
        width:float = 10, 
        height:float = 2, 
        cross_length:float = 1, 
        cross_width:float = 1, 
        x_translate:float = 0, 
        y_translate:float = 0
    ) -> cq.Workplane:
    work = cq.Workplane().rect(length, width)
    block = work.extrude(height)
    corners = (
        work
        .vertices().rect(length-cross_length,width-cross_width)
        .extrude(height)
    )

    result = block.cut(corners.translate((x_translate,y_translate,0)))

    # center
    result = result.translate((0,0,-1*(height/2)))

    return result
