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

def regular_polygon(radius=5, sides=6, height=5):
    polygon = (
        cq.Workplane("XY")
        .polygon(sides, radius)
    )

    if height:
        polygon = (
            polygon
            .extrude(height)
            .translate((0,0,-1*(height/2)))
        )

    meta = {'type':'regularPolygon','height':height, 'length':radius*2, 'width':radius*2}
    polygon.metadata = meta
    return polygon
