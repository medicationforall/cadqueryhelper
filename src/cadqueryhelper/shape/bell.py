# Copyright 2024 James Adams
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
from . import vase

def bell_outline(
        length:float = 25, 
        width:float = 10, 
        base_height:float = 4,
        base_inset:float = 3,
        mid_height:float = 18,
        top_inset:float = 2
    ) -> cq.Workplane:
    
    b_pnts = [
        (base_height,width-.1),
        (base_height+3,width-base_inset)
    ]
    
    m_points = [
        (base_height+mid_height+0.1,width-base_inset-(top_inset+.01)),
        (length+1, 0)
    ]
    
    result = (
        cq.Workplane()
        .lineTo(0,width)
        .lineTo(base_height,width)
        .threePointArc(b_pnts[0], b_pnts[1])
        .lineTo(base_height+3.01, width-base_inset)
        .lineTo(base_height+mid_height, width-base_inset-top_inset)
        .threePointArc(m_points[0], m_points[1])
        .lineTo(length, 0)
        .close()
    )
    
    return result

def bell(
        length:float = 25, 
        width:float = 10, 
        base_height:float = 4,
        base_inset:float = 3,
        mid_height:float = 18,
        top_inset:float = 2
    ):
    bell_ex = bell_outline(
        length, 
        width, 
        base_height,
        base_inset,
        mid_height,
        top_inset
    )

    bell_vase = vase(
        bell_ex, 
        workplane_axis="YZ",
        radius = 0.01
    )

    bell_ex_int = bell_outline(
        width=8,
        length= 23,
        mid_height=18,
        top_inset=2,
        base_height=1.5,
        base_inset=3
    )

    bell_vase_int = vase(
        bell_ex_int, 
        workplane_axis="YZ",
        radius = 0.01
    )

    return bell_vase.cut(bell_vase_int)