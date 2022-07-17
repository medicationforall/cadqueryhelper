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

def make_cube(length = 5, width = 5, height = 5 ):
    cube = cq.Workplane().box(length, width, height)
    return cube

def make_cylinder(radius = 2.5, height = 5 ):
    #cylinder = cq.Workplane().circle(diameter).extrude(height)
    cylinder = cq.Workplane().cylinder(height, radius)
    return cylinder

def make_hexagon(radius = 2.5, height = 5):
    cube = cq.Workplane().box(length, width, height)
    return cube

def make_cone():
    cone = cq.Solid.makeCone(1, 0, 2)
    return cone
