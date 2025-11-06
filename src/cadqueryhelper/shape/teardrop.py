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
from typing import Tuple

def teardrop(
        diameter:float = 5,
        length:float = 8,
        height:float|None = 3
    ):
    
    pts:list[Tuple[float,float]] = [
        (-length*.1,0),
        (0,length-.001),
        (length*.1,0)
    ]
    
    sk:cq.Sketch = (
        cq.Sketch()
        .push([(0,0)])
        .circle((diameter/2))
        .push([(0,diameter/2+.001)])
        .polygon(pts)
        .wires()
        .hull()
    )
    
    if height:
        part = (
            cq.Workplane("XY")
            .placeSketch(sk)
            .extrude(height)
        ).translate((0,0,-height/2))
    else:
        part = sk
        
    return part