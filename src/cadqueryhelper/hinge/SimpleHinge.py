import cadquery as cq
from cadqueryhelper import Base
from typing import Literal
from . import SimpleDoor, SimpleFrame, SimplePivot

class SimpleHinge(Base):
    def __init__(self):
        super().__init__()
        #parameters
        self.length:float = 40
        self.width:float = 4
        self.height:float = 42
        self.margin:float = 0.4
        self.frame_width:float = 1
        self.pivot_diameter:float = 3
        self.pivot_height:float|None = None
        self.door_width:float|None = None
        self.rotate_type:Literal['full','front','back'] = "full"
        self.rotate:float = 0
        
        #blueprints
        self.bp_door = SimpleDoor()
        self.bp_frame = SimpleFrame()
        self.bp_pivot = SimplePivot()
        
        #shapes
        self.outline:cq.Workplane|None = None
        
    def calculate_door_length(self):
        length = self.length - self.frame_width*2 - self.margin*2
        return length
    
    def calculate_door_width(self):
        width = self.width
        
        if self.door_width:
            width = self.door_width
        
        return width
    
    def calculate_door_height(self):
        height = self.height - self.frame_width*2 - self.margin*2
        return height

    def make_outline(self):
        outline = cq.Workplane("XY").box(
            self.length,
            self.width,
            self.height
        )
        
        self.outline = outline
        
    def make_frame(self):
        if self.bp_frame:
            bp_frame = self.bp_frame 
            bp_frame.length = self.length
            bp_frame.width = self.width
            bp_frame.height = self.height
            bp_frame.frame_width = self.frame_width
            bp_frame.make()
            
    def make_pivot(self):
        height = self.height
        if self.pivot_height:
            height = self.pivot_height

        if self.bp_pivot:
            bp_pivot = self.bp_pivot
            bp_pivot.height = height
            bp_pivot.diameter = self.pivot_diameter
            bp_pivot.margin = self.margin
            bp_pivot.make()
            
    def make_door(self):
        if self.bp_door:
            bp_door = self.bp_door
            bp_door.length = self.calculate_door_length()
            bp_door.width = self.calculate_door_width()
            bp_door.height =self.calculate_door_height()
            bp_door.rotate_type = self.rotate_type
            bp_door.make()
        
        
    def make(self):
        super().make()
        self.make_outline()
        self.make_frame()
        self.make_pivot()
        self.make_door()
        
    def build_outline(self)->cq.Workplane:
        super().build()

        part = cq.Workplane("XY")
        
        if self.outline:
            part = part.add(self.outline)
        
        return part
    
    def build_door(self):
        part = cq.Workplane("XY")
        length = self.calculate_door_length()
        x_translate = length/2 - self.calculate_door_width()/2

        if self.bp_door:
            door = self.bp_door.build()
            part = part.union(door.translate((x_translate,0,0)))

        if self.bp_pivot:
            pivot = self.bp_pivot.build()
            part = part.union(pivot)
            
        if self.rotate:
            part = part.rotate((0,0,1),(0,0,0),self.rotate)
        
        part = part.translate((-x_translate,0,0))
            
        return part
        
    def build(self)->cq.Workplane:
        super().build()
        part = cq.Workplane("XY")

        if self.bp_frame:
            frame = self.bp_frame.build()
            part = part.add(frame)
            
        if self.bp_pivot:
            length = self.calculate_door_length()
            x_translate = length/2 - self.calculate_door_width()/2

            cut_pivot = self.bp_pivot.build_cut()
            part = part.cut(cut_pivot.translate((-x_translate,0,0)))

        door = self.build_door()
        part = part.add(door)

        return part
    
    def build_cross_section(self)->cq.Workplane:
        scene = cq.Workplane("XY")
        door = self.build()
        outline = self.build_outline()
        
        scene = scene.add(door)
        scene = scene.cut(outline.translate((0,-self.width/2,0)))
        
        return scene