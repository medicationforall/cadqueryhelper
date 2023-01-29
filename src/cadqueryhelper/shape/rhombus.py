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

def rhombus(width = 10, offset = 4, height=5):
    points = [
        (0,0),
        (0,width),
        (width, width + offset),
        (width, 0 + offset)
        ]
    work = (
        cq.Workplane()
        .center(-(width/2),-(offset/2)-(width/2))
        .polyline(points).close()

    )
    if height:
        work = work.extrude(height)
        
    work = work.translate((0,0,-1*(height/2)))

    bounding_width = width

    if offset > -1:
        bounding_width += offset
    else:
        bounding_width += -1*offset

    meta = {'type':'rhombus','height':height, 'length':width, 'width':bounding_width}
    work.metadata = meta
    return work
