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
import math

def make_cube(length = 5, width = 5, height = 5 ):
    cube = cq.Workplane().box(length, width, height)
    return cube

def make_cylinder(radius = 2.5, height = 5 ):
    #cylinder = cq.Workplane().circle(diameter).extrude(height)
    cylinder = cq.Workplane().cylinder(height, radius)
    return cylinder

def __generate_hex_points(radius):
    '''
        https://stackoverflow.com/a/52172400
    '''
    hex_points = []
    for  i  in range(6):
        angle_deg = 60 * i - 30
        angle_rad = (math.pi / 180) * angle_deg;
        hex_points.append((radius * math.cos(angle_rad),
            radius * math.sin(angle_rad)))
    return hex_points

def make_hexagon(radius = 5, height = 5):
    points = __generate_hex_points(radius)
    work = cq.Workplane().polyline(points).close().extrude(5)
    return work

def make_cone():
    cone = cq.Solid.makeCone(1, 0, 2)
    return cone
