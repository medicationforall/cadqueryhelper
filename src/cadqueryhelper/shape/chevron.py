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

def chevron(
        length:float = 10, 
        width:float = 7, 
        height:float = 2, 
        inner_width:float = 3, 
        alt:bool = False
    ) -> cq.Workplane:
    if alt==False:
        points = [
            (0,inner_width),
            (length/2, width),
            (length, inner_width),
            (length, 0),
            (length/2, width -inner_width ),
            (0, 0)
        ]
    else:
        points = [
            (0,0),
            (length/2, width),
            (length, 0),
            (length-inner_width, 0),
            (length/2, width -inner_width ),
            (inner_width, 0)
        ]

    work = (
        cq.Workplane("XY")
        .polyline(points).close()
    )

    if height:
        work = work.extrude(height)

    # center, rotate
    work = work.translate((
        -1*(length/2),
        -1*(width/2),
        -1*(height/2)
    ))
    return work
