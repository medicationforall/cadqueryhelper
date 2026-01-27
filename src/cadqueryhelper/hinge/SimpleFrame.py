import cadquery as cq
from cadqueryhelper import Base

class SimpleFrame(Base):
    def __init__(self):
        super().__init__()
        #parameters
        self.length:float = 30
        self.width:float = 25
        self.height:float = 60
        self.frame_width:float = 1

        #shapes
        self.outline:cq.Workplane|None = None
        self.frame:cq.Workplane|None = None

    def make_frame(self):
        length = self.length
        width = self.width
        height = self.height
        frame_width = self.frame_width

        frame = cq.Workplane("XY").box(
            length,
            width,
            height
        )
        
        int_length = length - frame_width * 2
        int_height = height - frame_width * 2
        inner_cut = cq.Workplane("XY").box(
            int_length,
            width,
            int_height
        )
        
        frame = (
            frame
            .cut(inner_cut)
        )

        self.frame = frame

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
        self.make_frame()
        
    def build_outline(self)->cq.Workplane:
        super().build()
        
        part = cq.Workplane("XY")
        
        if self.outline:
            part = part.add(self.outline)
        
        return part
        
    def build(self)->cq.Workplane:
        super().build()
        
        part = cq.Workplane("XY")
        
        if self.frame:
            part = part.add(self.frame)
        
        return part