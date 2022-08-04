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

import cqmore as cqm
from cqmore.polygon import star

#
def make_cone():
    cone = cq.Solid.makeCone(1, 0, 2)
    return cone


def make_triangle(radius = 5, height = 5):
    points = __generate_polygon_points(radius, 3, 60, 90)
    work = cq.Workplane().polyline(points).close().extrude(height)

    meta = {'type':'triangle', 'radius':radius, 'height':height, 'length':radius*2, 'width':radius*2}
    work.metadata = meta
    return work

#
def make_cube(length = 5, width = 5, height = 5 ):
    work = cq.Workplane().box(length, width, height)

    meta = {'type':'cube', 'length':length, 'width':width, 'height':height}
    work.metadata = meta
    return work
#
def make_pentagon(radius = 5, height = 5):
    '''
        5 sided polygon
    '''
    points = __generate_polygon_points(radius, 5, 72, 180)
    work = cq.Workplane().polyline(points).close().extrude(height)

    meta = {'type':'pentagon', 'radius':radius, 'height':height, 'length':radius*2, 'width':radius*2}
    work.metadata = meta
    return work
#
def make_hexagon(radius = 5, height = 5):
    '''
        6 sided polygon
    '''
    points = __generate_polygon_points(radius, 6, 60, 180)
    work = cq.Workplane().polyline(points).close().extrude(height)

    meta = {'type':'hexagon', 'radius':radius, 'height':height, 'length':radius*2, 'width':radius*2}
    work.metadata = meta
    return work
#
def make_heptagon(radius = 10, height = 5):
    '''
        7 sided polygon
    '''
    points = __generate_polygon_points(radius, 7, 51.428571428571428571428571428571, 180)
    work = cq.Workplane().polyline(points).close().extrude(height)

    meta = {'type':'heptagon', 'radius':radius, 'height':height, 'length':radius*2, 'width':radius*2}
    work.metadata = meta
    return work
#
def make_octagon(radius = 10, height = 5):
    '''
        8 sided polygon
    '''
    points = __generate_polygon_points(radius, 8, 45, 180)
    work = cq.Workplane().polyline(points).close().extrude(height)

    meta = {'type':'octagon', 'radius':radius, 'height':height, 'length':radius*2, 'width':radius*2}
    work.metadata = meta
    return work
#
def make_nonagon(radius = 10, height = 5):
    '''
        9 sided polygon
    '''
    points = __generate_polygon_points(radius, 9, 40, 180)
    work = cq.Workplane().polyline(points).close().extrude(height)

    meta = {'type':'nonagon', 'radius':radius, 'height':height, 'length':radius*2, 'width':radius*2}
    work.metadata = meta
    return work

#
def make_cylinder(radius = 2.5, height = 5 ):
    #cylinder = cq.Workplane().circle(diameter).extrude(height)
    work = cq.Workplane().cylinder(height, radius)

    meta = {'type':'cylinder', 'radius':radius, 'height':height, 'length':radius*2, 'width':radius*2}
    work.metadata = meta
    return work

#
def make_rhombus(width = 10, offset = 4, height=5):
    points = [
        (0,0),
        (0,width),
        (width, width + offset),
        (width, 0 + offset)
        ]
    work = cq.Workplane().center(-(width/2),-(offset/2)-(width/2)).polyline(points).close().extrude(height)

    meta = {'type':'rhombus','height':height, 'length':width, 'width':width+offset}
    work.metadata = meta
    return work

#
def make_sphere(radius = 5):
    diameter = radius * 2
    work = cq.Workplane().sphere(radius)

    meta = {'type':'sphere','height':diameter, 'length':diameter, 'width':diameter}
    work.metadata = meta
    return work

#
def make_star(outer_radius = 10, inner_radius = 5, points = 5, height = 3):
    diameter = outer_radius * 2
    work = cqm.Workplane().makePolygon(star(outerRadius = outer_radius, innerRadius = inner_radius, n = points)).extrude(height)
    meta = {'type':'star','height':height, 'length':outer_radius*2, 'width':outer_radius*2}
    work.metadata = meta
    return work

def __generate_polygon_points(radius, point_count, deg, rad):
    '''
        https://stackoverflow.com/a/52172400
    '''
    points = []
    for  i  in range(point_count):
        angle_deg = deg * i
        angle_rad = (math.pi / rad) * angle_deg;
        points.append((radius * math.cos(angle_rad),
            radius * math.sin(angle_rad)))
    return points
