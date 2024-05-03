# Copyright 2023 James Adams
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

def lightning(
        length:float = 25, 
        width:float = 50, 
        height:float = 5, 
        x_dist:float = 3, 
        y_dist:float = 6
    ) -> cq.Workplane:
    x_actual = x_dist + y_dist
    pts = [
        (0,0),# origin point
        (length, width/2+y_dist),
        (0+x_actual, width/2),
        (length, width),# top point
        (0, width/2-y_dist),
        (length-x_actual, width/2),
    ]

    shape = (
        cq.Workplane("XY")
        .polyline(pts).close()
        .extrude(height)
        .translate((-1*(length/2),-1*(width/2),-1*height/2))

    )

    return shape
