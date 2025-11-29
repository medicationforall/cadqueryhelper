# Copyright 2025 James Adams
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

def ring(
        diameter:float = 100, 
        inner_diameter:float = 80, 
        height:float = 4
    ) -> cq.Workplane:
    if inner_diameter >= diameter:
        raise Exception(f"{inner_diameter=} needs to be less than {diameter=}")
    
    outside = cq.Workplane("XY").cylinder(height, diameter / 2)
    inside = cq.Workplane("XY").cylinder(height, inner_diameter / 2)
    ring = outside.cut(inside)
    
    return ring
