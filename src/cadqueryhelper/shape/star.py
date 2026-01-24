# Copyright 2026 James Adams
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
from cadqueryhelper.shape import make_circular_points, interweave_lists

def star(
        outer_radius:float = 10, 
        inner_radius:float = 5, 
        points:int = 5, 
        height:float = 3,
        rotate = None
    ) -> cq.Workplane:
    
    if rotate == None:
        rotate = (360 / points)/2

    arc, outer_points = make_circular_points(outer_radius, 0, points)
    arc, inner_points = make_circular_points(inner_radius, rotate, points)

    list_points = interweave_lists([outer_points, inner_points])
    result = cq.Workplane("XY").polyline(list_points).close()
    
    if height:
        result = result.extrude(height).translate((0,0,-(height/2)))

    return result

ex_star = star(points = 9)

