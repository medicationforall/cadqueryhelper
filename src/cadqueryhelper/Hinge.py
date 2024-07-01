# Copyright 2023 James Adams
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
from . import Base
from typing import Literal

class Hinge(Base):
    def __init__(self):
        super().__init__()
        #parameters
        self.length:float = 40
        self.radius:float = 2
        self.segments:int = 4 
        self.pad:float = 1

        self.base_inset:float = 0.6
        self.key_length:float = 1.5
        self.key_width:float = 0.5

        self.tab_length:float = 10
        self.tab_height:float|None = None
        self.tab_z_translate:float = 0

        self.rotate_deg:float = 0
        self.plate_spacer:float = 0.4
        
        self.render:Literal['both', 'receiver', 'driver'] = "both"
        self.invert: bool = False

        #parts
        self.h_parts:cq.Workplane|None = None
        self.join_plate:cq.Workplane|None = None

    def _calculate_tab_height(self) -> float:
        if self.tab_height:
            tab_height = self.tab_height
        else:
            tab_height = self.radius
        return tab_height
        
    def __make_driver(
            self, 
            length:float
        ):
        points = [
            (0,0),
            (length,0),
            (length,self.base_inset),
            (length+self.key_length, self.radius-self.key_width),
            (length+self.key_length, self.radius),
            (0-self.key_length, self.radius),
            (0-self.key_length, self.radius-self.key_width),
            (0,self.base_inset)
        ]
        
        cyl = (
            cq.Workplane("XY")
            .center(0,0)
            .polyline(points).close()
            .translate((-1*((length)/2),-self.radius,0))
            .revolve(360,(0,self.radius,0),(1,self.radius,0))
        ).translate((-length/2,-self.radius,0))
        
        return cyl
    
    def __make_receiver(
            self,
            length:float
        ):
        points = [
            (0,0),
            (length,0),
            (length,self.base_inset),
            (length-self.key_length, self.radius-self.key_width),
            (length-self.key_length, self.radius),
            (0+self.key_length, self.radius),
            (0+self.key_length, self.radius-self.key_width),
            (0,self.base_inset)
        ]
        
        cyl = (
            cq.Workplane("XY")
            .center(0,0)
            .polyline(points).close()
            .translate((-1*((length)/2),-self.radius,0))
            .revolve(360,(0,self.radius,0),(1,self.radius,0))
        ).translate((-length/2,-self.radius,0))
        return cyl
    
    def __make_tab(
            self, 
            length:float, 
            side:int
        ):
        
        if self.invert ==  True:
            direction = -1
            if side:
                direction = 1
        else:
            direction = 1
            if side:
                direction = -1
            
        cut_cylinder = (
            cq.Workplane("XY")
            .cylinder(length, self.radius-.1).rotate((0,1,0),(0,0,0),90)
        )

        tab_height = self._calculate_tab_height()  
        tab = (
            cq.Workplane("XY")
            .box(length,self.tab_length,tab_height)
        ).translate((0,direction*(self.tab_length/2),-(tab_height/2)+ self.tab_z_translate))
        return tab.cut(cut_cylinder)
        
    def __hinge_cylinder(
            self, 
            length:float, 
            side:int
        ):
        
        if side:
            cyl = self.__make_driver(length)
        else:
            cyl = self.__make_receiver(length)

        tab = self.__make_tab(length, side)
        combined = cyl.union(tab)
        
        if (not self.invert and not side) or (self.invert and side):
            combined = combined.rotate((1,0,0),(0,0,0),self.rotate_deg)
        return combined
    
    def __should_render(self, part_type="driver"):
        if self.render == 'both' or part_type == self.render:
            return True
        else:
            return False

    def __make_segments(self):
        segment_length = self.length/self.segments
        h_parts = cq.Workplane("XY")
        
        driver = self.__hinge_cylinder(
            length = segment_length-self.pad/2,
            side =  1 if self.invert else 0
        )
        
        receiver = cyl = self.__hinge_cylinder(
            length = segment_length-self.pad/2,
            side = 0 if self.invert else 1
        )
        
        for i in range(0,self.segments):
            
            if i % 2 == 0:
                part_type ="receiver"
                cyl = receiver
            else:
                part_type ="driver"
                cyl = driver
        
            if i == self.segments -1:
                #log(f"end {segment_length-pad/2}")
                cyl = cyl.translate((self.pad/4,0,0))
            elif i == 0:
                #log(f"begin {segment_length-pad/2}")
                cyl = cyl.translate((-self.pad/4,0,0))
                
            
            if self.__should_render(part_type):
                h_parts = h_parts.add(cyl.translate(((segment_length)*i,0,0)))
            
        h_parts = h_parts.translate((segment_length/2-self.length/2,0,0))
        self.h_parts = h_parts
        
    def __make_join_plate(self):
        tab_height = self._calculate_tab_height()

        join_plate = (
            cq.Workplane("XY")
            .box(
                self.length,
                self.tab_length-self.radius-self.plate_spacer, 
                tab_height
            )
            .translate((0,0,-(tab_height/2) + self.tab_z_translate))
        )
        self.join_plate = join_plate
        
    def make(self, parent=None):
        super().make(parent)
        self.__make_segments()
        self.__make_join_plate()

    def build(self) -> cq.Workplane:
        super().build()
        p_x_translate = (self.tab_length/2)+(self.radius+self.plate_spacer)/2
        hinge_build = cq.Workplane("XY")

        if self.h_parts:
            hinge_build = (
                hinge_build
                .union(self.h_parts)
            )

        if self.join_plate:
            
            if self.__should_render('driver'):
                hinge_build = (
                    hinge_build
                    .union(self.join_plate.translate((0,p_x_translate,0)).rotate((1,0,0),(0,0,0),self.rotate_deg))
                )
            
            if self.__should_render('receiver'):
                hinge_build = (
                    hinge_build
                    .union(self.join_plate.translate((0,-1*p_x_translate,0)))
                )
        return hinge_build
