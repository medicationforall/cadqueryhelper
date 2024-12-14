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

def vase(
        shape:cq.Workplane, 
        workplane_axis:str = "YZ", #'XY', 'YZ', 'XZ'
        radius:float = 1, 
        angle:float = 0, 
        rotation_angle:float = 0
    ) -> cq.Workplane:
    '''
    Assumed the shape is centered on the XY plane.
    '''
    path = (
        cq.Workplane(workplane_axis)
        .center(0,0)
        .ellipseArc(
            radius,
            radius,
            angle,
            rotation_angle = rotation_angle
        )
    )
    sweep = shape.sweep(path).translate((radius,0,0))
    return sweep