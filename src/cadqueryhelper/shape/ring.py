import cadquery as cq

def ring(diameter:float = 100, inner_diameter:float = 80, height:float = 4):
    if inner_diameter >= diameter:
        raise Exception(f"{inner_diameter=} needs to be less than {diameter=}")
    
    outside = cq.Workplane("XY").cylinder(height, diameter / 2)
    inside = cq.Workplane("XY").cylinder(height, inner_diameter / 2)
    ring = outside.cut(inside)
    
    return ring
