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
from cadqueryhelper import Base, shape, wave

class HelperPlate(Base):
    def __init__(self):
        super().__init__()
        
        # shapes
        self.shapes = []
        
    def __make_shapes(self):
        arch_round = shape.arch_round(
            length=30, 
            width=5, 
            height=50
        )
        self.shapes.append(arch_round.translate((0,0,10)))
        
        arch = shape.arch_pointed(
            length=30, 
            width=5, 
            height=50, 
            inner_height=25
        )
        self.shapes.append(arch.translate((0,0,10)))
        
        arrow = shape.arrow(
            length=30, 
            inner_length=15, 
            width=15, 
            width_outset=5, 
            height=3
        )
        self.shapes.append(arrow)
        
        chevron = shape.chevron(
            length=25, 
            width=25, 
            height=3, 
            inner_width=5, 
            alt=False
        )
        self.shapes.append(chevron)
        
        chevron_alt = shape.chevron(
            length=25, 
            width=25, 
            height=3, 
            inner_width=5, 
            alt=True
        )
        self.shapes.append(chevron_alt)
        
        #--------------
        
        coffin = shape.coffin(
            length = 25, 
            width = 30,
            height =3,
            top_length = 10,
            base_length = 15, 
            mid_offset = 5
        )
        self.shapes.append(coffin)
        
        cone = shape.cone(
            radius=15, 
            radius_top=0, 
            height=15
        )
        self.shapes.append(cone)
        
        corner_join = shape.corner_join(
            length = 25,
            width = 15,
            height = 10,
            side_width = 3,
            corner_chamfer = 2
        )
        self.shapes.append(corner_join)
        
        cross = shape.cross(
            length=25, 
            width=25, 
            height=5, 
            cross_length=3, 
            cross_width=3, 
            x_translate=0, 
            y_translate=0
        )
        self.shapes.append(cross)
        
        cube = shape.cube(
            length=15, 
            width=15, 
            height=15
        )
        self.shapes.append(cube)
        
        #--------------
        
        cylinder = shape.cylinder(
            radius=10, 
            height=10
        )
        self.shapes.append(cylinder)
        
        diamond = shape.diamond(
            length=25, 
            width=15, 
            height=3
        )
        self.shapes.append(diamond)
        
        heptagon = shape.regular_polygon(
            radius=30, 
            sides=7
        )
        self.shapes.append(heptagon)
        
        hexagon = shape.regular_polygon(
            radius=30,
            sides=6
        )
        self.shapes.append(hexagon)
        
        i_beam = shape.i_beam(
            length=40,
            width=10,
            height=15,
            web_thickness=2,
            flange_thickness=2,
            join_distance=1.3
        )
        self.shapes.append(i_beam)
        
        #--------------
        
        jersey = shape.jersey_barrier(
            length=40,
            width = 20,
            height = 20,
            base_height = 4,
            middle_width_inset = -4,
            middle_height = 2,
            top_width_inset = -1
        )
        
        self.shapes.append(jersey)
        
        lightning = shape.lightning(
            length = 20,
            width = 40,
            height = 5,
            x_dist = 2,
            y_dist = 3
        )
        self.shapes.append(lightning)
        
        nonagon  = shape.regular_polygon(
            radius=30, 
            sides=9
        )
        self.shapes.append(nonagon)
        
        octagon = shape.regular_polygon(
            radius=30, 
            sides=8
        )
        self.shapes.append(octagon)
        
        pentagon = shape.regular_polygon(
            radius=30, 
            sides=5
        )
        self.shapes.append(pentagon)
        
        ring_params = []
        ring_params.append({"radius": 25, "start_angle":0})
        ring_params.append({"radius":20,"start_angle":30})
        ring_params.append({"radius":5,"start_angle":80})
        
        #--------------
        
        pinwheel = shape.pinwheel(
            count = 10, 
            height = 3, 
            ring_params = ring_params
        )
        self.shapes.append(pinwheel)
        
        
        test_shape = cq.Workplane('XY').rect(4,8)
        pst = pts = [(0,0), (20,-20), (50,-20), (50,-30)]
        pipe = shape.pipe(test_shape, pts)
        self.shapes.append(pipe.translate((-25,0,15)))
        
        rail = shape.rail(
            length=40, 
            width=10, 
            height=25, 
            inner_height=5
        )
        
        self.shapes.append(rail)
        
        
        rhombus = shape.rhombus(
            width=30, 
            offset=20, 
            height=5
        )
        
        self.shapes.append(rhombus)
        
        
        sphere = shape.sphere(
            radius=15
        )
        
        self.shapes.append(sphere.translate((0,0,10)))
        
        #--------------
        
        star = shape.star(
            outer_radius=25,
            inner_radius=10,
            points=5,
            height=3
        )
        
        self.shapes.append(star)
        
        trapezoid = shape.trapezoid(
            length = 35,
            width = 25,
            height = 25,
            top_width = 10
        )
        
        self.shapes.append(trapezoid)
        
        shape_wave = wave.sine(
            length=8,
            width=5,
            height=0,
            segment_length=3,
            inner_width=2
        )
        
        ripple = shape.vase(
            shape_wave, 
            workplane_axis = "YZ",
            radius = 1, 
            angle=0, 
            rotation_angle=0
        )
        
        self.shapes.append(
            ripple.rotate((0,1,0),(0,0,0),90)
            .translate((0,0,-2))
        )
        
        sine_wave = wave.sine(
            length=8,
            width=10,
            height=0,
            segment_length=3,
            inner_width=5
        )
        
        vase = shape.vase(
            sine_wave,
            workplane_axis = "XZ",
            radius = 1, 
            angle=0, 
            rotation_angle=0
        )
        self.shapes.append(vase.rotate((1,0,0),(0,0,0),-90).translate((0,0,-5)))

        
    def make(self, parent=None):
        super().make(parent)
        self.backdrop = shape.backdrop(length=500)
        self.__make_shapes()

        
    def build(self):
        super().build()
        scene = (
            cq.Workplane("XY")
            .union(self.backdrop.translate((0,0,60)))
        )
        
        shapes = cq.Workplane("XY")
        
        column = -1
        for i,shape in enumerate(self.shapes):
            if i %5 ==0:
                column+=1
            shapes = shapes.union(shape.translate(((column)*50,(i%5)*-40,0)))
        
        return scene.union(shapes.translate((-((5*50)/2),((4*40)/2),0)))
    
    def build_assembly(self):
        shapes = cq.Workplane("XY")
        
        column = -1
        for i,shape in enumerate(self.shapes):
            if i %5 ==0:
                column+=1
            shapes = shapes.union(shape.translate(((column)*50,(i%5)*-40,0)))
        
        assembly = cq.Assembly()
        assembly.add(self.backdrop.translate((0,0,60)), color=cq.Color(1, 1,1 ), name="backdrop")
        assembly.add(shapes.translate((-((5*50)/2),((4*40)/2),0)), color=cq.Color(0, 0, 1), name="shapes")
        return assembly