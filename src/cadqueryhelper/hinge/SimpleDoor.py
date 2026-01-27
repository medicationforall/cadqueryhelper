import cadquery as cq
from cadqueryhelper import Base
from cadqueryhelper.shape import cylinder_sector
from typing import Literal

class SimpleDoor(Base):
    def __init__(self):
        super().__init__()
        #parameters
        self.length:float = 30
        self.width:float = 4
        self.height:float = 40
        self.rotate_type:Literal['full','front','back'] = 'full'#front,back
        
        self.bp_door:Base|None = None

        #shapes
        self.outline:cq.Workplane|None = None
        self.clearance:cq.Workplane|None = None
        self.cut_clearance:cq.Workplane|None = None
        self.door:cq.Workplane|None = None

    def make_clearance(self):
        w = self.width
        h = self.height #- margin * 2
        
        clearance = cylinder_sector(
            diameter = w,  
            angle = 180,
            height = h
        ).translate((0,0,-h/2)).rotate((0,0,1),(0,0,0),-90)

        self.clearance = clearance
        
    def make_clearance_90(self):
        w = self.width
        h = self.height #- margin * 2
        
        clearance = cylinder_sector(
            diameter = w,  
            angle = 90,
            height = h
        ).translate((0,0,-h/2)).rotate((0,0,1),(0,0,0),-90)
        
        clearance = (
            clearance
            .rotate((1,0,0),(0,0,0),-90)
            .faces(">Z")
            .extrude(w/2)
        )
        
        if self.rotate_type is "front":
            clearance = (
                clearance
                .rotate((1,0,0),(0,0,0),-90)
                .translate((0,w/2,0))
            )
        else:
            clearance = (
                clearance
                .rotate((1,0,0),(0,0,0),90)
                .translate((0,-w/2,0))
            )
            
        self.clearance = clearance

    def make_cut_clearance(self):
        w = self.width
        h = self.height #- margin * 2
        cut_clearance = cq.Workplane("XY").box(w/2,w,h).translate((-w/4,0,0))
        self.cut_clearance = cut_clearance

    def make_door(self):
        l = self.length #- margin * 2
        w = self.width
        h = self.height #- margin * 2
        
        if not self.bp_door:
            door = cq.Workplane("XY").box(l, w, h)
        else:
            if hasattr(self.bp_door,'length') and hasattr(self.bp_door,'width') and hasattr(self.bp_door,'height'):
                self.bp_door.length = l
                self.bp_door.width = w
                self.bp_door.height = h
            self.bp_door.make()
            door = self.bp_door.build()
        self.door = door
        
    def make_outline(self):
        outline = cq.Workplane("XY").box(
            self.length,
            self.width,
            self.height
        )
        
        self.outline = outline
        
    def make(self):
        super().make()
        self.make_outline()
        self.make_cut_clearance()
        if self.rotate_type is 'full':
            self.make_clearance()
        else:
            self.make_clearance_90()
        self.make_door()
        
    def build_outline(self)->cq.Workplane:
        super().build()

        part = cq.Workplane("XY")
        
        if self.outline:
            part = part.add(self.outline)
        
        return part
         
    def build(self)->cq.Workplane:
        super().build()

        scene = cq.Workplane("XY")
        
        if self.door and self.cut_clearance and self.clearance:
            l = self.length #- margin * 2
            scene = (
                scene
                .union(self.door)
                .cut(self.cut_clearance.translate((-l/2+self.width/2,0,0)))
                .union(self.clearance.translate((-l/2+self.width/2,0,0)))
             )
        
        return scene