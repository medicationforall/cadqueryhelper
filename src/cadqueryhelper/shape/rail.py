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

def rail(
        length:float = 6, 
        width:float = 1, 
        height:float = 5, 
        inner_height:float = 1.5
    ) -> cq.Workplane:
    points = [
        (0,0),
        (0, inner_height),
        (length, height),
        (length, height - inner_height)
    ]

    work = (
        cq.Workplane()
        .center(-(length/2),-(height/2))
        .polyline(points).close()
    )

    if width:
        work = work.extrude(width)

    # center, rotate
    work = work.translate((0,0,-1*(width/2)))
    work = work.rotate((1, 0, 0), (0, 0, 0), -90)

    return work
