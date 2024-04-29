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
import cqmore as cqm
from cqmore.polygon import star as cqmStar

def star(
        outer_radius:float = 10, 
        inner_radius:float = 5, 
        points:int = 5, 
        height:float = 3
    ) -> cqm.Workplane:
    diameter = outer_radius * 2
    work = (
        cqm.Workplane()
        .makePolygon(cqmStar(outerRadius = outer_radius, innerRadius = inner_radius, n = points))
    )

    if height:
        work = work.extrude(height)

    work = work.translate((0,0,-(height/2)))
    return work
