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

def cross(length=10, width=10, height=2, cross_length=1, cross_width=1, x_translate=0, y_translate=0):
    work = cq.Workplane().rect(length, width)
    block = work.extrude(height)
    vertices = work.vertices()
    corners = (
        work
        .vertices().rect(length-cross_length,width-cross_width)
        .extrude(height)
    )

    result = block.cut(corners.translate((x_translate,y_translate,0)))

    # center
    result = result.translate((0,0,-1*(height/2)))

    meta = {'type':'arrow','height':height, 'length':length, 'width':width}
    result.metadata = meta

    return result
