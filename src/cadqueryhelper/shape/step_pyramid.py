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

def step_pyramid(
    length:float = 40,
    width:float = 60,
    height:float = 30,
    steps:int = 3,
    min_length:float = 10,
    min_width:float = 15,
    ellipse:bool = False
) -> cq.Workplane:
    pyramid = cq.Workplane("XY")
    l_height = height/steps
    length_step = (length-min_length)/(steps-1)
    width_step = (width-min_width)/(steps-1)
    total_height = 0

    for i in range(steps):
        l_length = length - length_step*i
        l_width = width - width_step*i

        if ellipse:
            sk = cq.Sketch().ellipse(l_length,l_width)
            layer = (
                cq.Workplane("XY")
                .placeSketch(sk)
                .wire()
                .extrude(l_height)
            )
        else:
            layer = cq.Workplane("XY").box(
                l_length,
                l_width,
                l_height
            ).translate((0,0,l_height/2))
        
        pyramid = pyramid.union(layer.translate((0,0,total_height)))
        total_height+=l_height
        
    return pyramid