import cadquery as cq
from cadqueryhelper import Base

class SimplePivot(Base):
    def __init__(self):
        super().__init__()
        #parameters
        self.diameter:float = 4 
        self.height:float = 43
        self.margin:float = 0.4 

        #shapes
        self.outline:cq.Workplane|None = None
        self.pivot:cq.Workplane|None = None
        self.cut_pivot:cq.Workplane|None = None

    def make_pivot(self):
        height = self.height
        diameter = self.diameter
        pivot  = cq.Workplane("XY").cylinder(
            height,
            diameter/2
        )

        self.pivot = pivot

    def make_cut_pivot(self):
        height = self.height + self.margin #* 2 # I may want this higher
        diameter = self.diameter + self.margin
        pivot  = cq.Workplane("XY").cylinder(
            height,
            diameter/2
        )

        self.cut_pivot = pivot

    def make_outline(self):
        outline = cq.Workplane("XY").cylinder(
            self.height,
            self.diameter/2
        )
        
        self.outline = outline
        
    def make(self):
        super().make()
        self.make_outline()
        self.make_pivot()
        self.make_cut_pivot()
        
    def build_outline(self)->cq.Workplane:
        super().build()
        
        part = cq.Workplane("XY")
        
        if self.outline:
            part = part.union(self.outline)
        
        return part
    
    def build_cut(self)->cq.Workplane:
        super().build()
        
        part = cq.Workplane("XY")
        
        if self.cut_pivot:
            part = part.union(self.cut_pivot)
        
        return part
        
    def build(self)->cq.Workplane:
        super().build()
        
        part = cq.Workplane("XY")
        
        if self.pivot:
            part = part.union(self.pivot)
        
        return part