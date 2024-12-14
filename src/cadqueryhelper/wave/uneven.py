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
import random
from numpy import arange
from typing import List

def uneven(
    length:float = 10, 
    width:float = 2.5,
    min_width:float = 0.0001,
    step:float = .5,
    count:tuple[int,int]|int = (2,8), 
    axis:str = "XY",
    seed:str|None = None,
    offset:float = 0
):
    if seed:
        random.seed(seed)

    pts:List[tuple[float,float]] = [(0, 0)]
    widths = arange(min_width, width+step, step)
    
    if type(count)==tuple:
        #log('count is tuple')
        counts = range(count[0],count[1])
        pt_count:int = random.choice(counts)
    elif type(count) == int:
        pt_count:int = count
    else:
        raise Exception("Uneven count is an Unrecognized type")
        
    interval = length/pt_count
        
    for i in range(pt_count):
        #log(f'test {i}')
        l = i * interval
        w = random.choice(widths)
        #log(f'{i} width = {w}')
             
        pts.append((l,w))
    
    pts = pts + [(length, 0)]
    
    result:cq.Workplane = (
        cq.Workplane(axis)
        .workplane(offset=offset)
        .center(-length/2,-width/2)
        .polyline(pts)
        .close()
    )
    return result