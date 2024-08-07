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

def arch_pointed(
        length:float = 30, 
        width:float = 5, 
        height:float = 50, 
        inner_height:float = 25
    ) -> cq.Workplane:

    m_length = length/2 #mirror length
    sPnts = [
        (inner_height+.00001, m_length+0),
        (height, 0)
    ]

    result = (
        cq.Workplane("XY")
        .lineTo(0, m_length)
        .lineTo(inner_height, m_length)
        .spline(sPnts, includeCurrent=True)
        .close().mirrorX()
    )

    if width:
        result = result.extrude(width)

    # center
    result = result.translate((-1*(height/2),0,-1*(width/2)))
    result = result.rotate((0, 1, 0), (0, 0, 0), 90)
    result = result.rotate((0, 0, 1), (0, 0, 0), 90)

    return result

def arch_round(
        length:float = 30, 
        width:float = 5, 
        height:float = 50
    ) -> cq.Workplane:
    #create the initial shape
    arch = (cq.Workplane("XY")
              .box(length, width, height)
              .translate((0,0,(height/2)))
              )

    # round off the top
    arch = arch.faces("Z").edges("Y").fillet((length/2)-.01)

    return arch.translate((0,0,-1*(height/2)))
