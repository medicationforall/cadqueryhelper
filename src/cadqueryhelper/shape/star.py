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

def star(outer_radius = 10, inner_radius = 5, points = 5, height = 3):
    diameter = outer_radius * 2
    work = cqm.Workplane().makePolygon(cqmStar(outerRadius = outer_radius, innerRadius = inner_radius, n = points)).extrude(height)
    meta = {'type':'star','height':height, 'length':outer_radius*2, 'width':outer_radius*2}
    work.metadata = meta
    return work
