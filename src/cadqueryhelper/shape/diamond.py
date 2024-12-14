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

def diamond(
        length:float = 6, 
        width:float = 4, 
        height:float = 2
    ) -> cq.Workplane:
    points = [
        (length/2,0),
        (length, width/2 ),
        (length/2, width),
        (0, width/2)
    ]

    work = (
        cq.Workplane("XY")
        .polyline(points).close()
    )

    if height:
        work = work.extrude(height)

    # center
    work = work.translate((
        -1*(length/2),
        -1*(width/2),
        -1*(height/2
    )))
    return work
