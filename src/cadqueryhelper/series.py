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
from typing import Callable

def series(
        shape:cq.Workplane, 
        size:int = 5, 
        length_offset:float|None = None, 
        width_offset:float|None = None, 
        height_offset:float|None = None, 
        skip_last:int = 0, 
        skip_first:int = 0, 
        operation: Callable[[cq.Workplane, int, int, dict], cq.Workplane]|None=None,
        union:bool=False
    ) -> cq.Workplane:
    series = cq.Workplane('XY')
    length, width, height = __resolve_hit_box(shape)

    bounding_box = {
        "length":length,
        "width":width,
        "height":height
    }

    for i in range(size):
        x_coord = 0
        y_coord = 0
        z_coord = 0

        if length_offset != None:
            x_coord = i * (length + length_offset)
            if i != 0:
                bounding_box['length'] += length + length_offset

        if width_offset != None:
            y_coord = i * (width + width_offset)
            if i != 0:
                bounding_box['width'] += width + width_offset

        if height_offset != None:
            z_coord = i * (height + height_offset)
            if i != 0:
                bounding_box['height'] += height + height_offset

        if i < size-skip_last:
            if i >= skip_first:
                series_shape = shape
                if operation:
                    series_shape = operation(shape, size, i, bounding_box)
                    
                # Would rather use union operation by default for performance 
                # instead using add operation
                # based on assumed interaction with the stack
                # e.g. skirmishbunker
                if(union):
                    series = series.union(series_shape.translate((
                        x_coord, 
                        y_coord, 
                        z_coord
                    )))
                else:
                    series = series.add(series_shape.translate((
                        x_coord, 
                        y_coord, 
                        z_coord
                    )))
            else:
                print('skipping first series tile')
        else:
            print('skipping last series tile')

    x_translate = 0
    y_translate = 0
    z_translate = 0
    
    if length_offset != None:
        x_translate = ((size-1)*(length + length_offset))/2
    
    if width_offset != None:
        y_translate = ((size-1)*(width + width_offset))/2

    if height_offset != None:
        z_translate = ((size-1)*(height + height_offset))/2
    return series.translate((-x_translate,-y_translate, -(z_translate)))

def __resolve_hit_box(
        shape:cq.Workplane
    ) -> tuple[float,float,float]:
    bounds = shape.val().BoundingBox() #type: ignore
    if bounds:
        length = bounds.xlen
        width = bounds.ylen
        height = bounds.zlen
    else:
        raise Exception('Could not resolve for bounding box')
    return length, width, height
