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

def arrow(length=10, inner_length=5, width=5, width_outset=2, height=3):
    points = [
        (0,0),
        (0,width),
        (inner_length, width),
        (inner_length, width+width_outset),
        (length, width/2),
        (inner_length, 0-width_outset),
        (inner_length, 0),
        ]
    work = cq.Workplane().center(0,0).polyline(points).close().extrude(height)

    # zero out the offset caused by the first node
    y_offset = 0

    if width_outset > 0:
         y_offset = width_outset
    work = work.translate((0,y_offset,0))

    # center shape
    box_width = width+y_offset+y_offset

    # center shape
    work = work.translate((-1*(length/2),-1*(box_width/2),-1*(height/2)))

    #todo need to address width when outset is positive
    meta = {'type':'arrow','height':height, 'length':length, 'width':box_width}
    work.metadata = meta
    return work
