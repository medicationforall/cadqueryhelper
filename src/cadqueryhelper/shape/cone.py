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

def cone(
        radius:float = 1, 
        radius_top:float = 0, 
        height:float = 2
    ) -> cq.Workplane:
    #https://cadquery.readthedocs.io/en/latest/classreference.html#cadquery.Solid.makeCone
    cone = cq.Solid.makeCone(radius, radius_top, height)

    # center shape
    work = cq.Workplane().add(cone)
    work = work.translate((0,0,-1*(height/2)))

    return work
