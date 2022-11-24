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

def arch_pointed(length=30, width=5, height=50, inner_height=25):
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
        .close().mirrorX().extrude(width)
    )

    # center
    result = result.translate((-1*(height/2),0,-1*(width/2)))
    result = result.rotate((0, 1, 0), (0, 0, 0), 90)
    result = result.rotate((0, 0, 1), (0, 0, 0), 90)

    meta = {'type':'arch', 'height':height, 'length':length, 'width':width}
    result.metadata = meta

    return result
