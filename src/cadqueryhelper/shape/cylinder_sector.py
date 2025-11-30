import cadquery as cq

def cylinder_sector(
    diameter:float = 20,  
    angle:float = 30,
    height:float = 5
):
    
    length = diameter/2
    width = diameter/2
    
    sector = (
        cq.Workplane("XY")
        .lineTo(length,0)
        .ellipseArc(length,width, 0, angle)
        .close()
    )
    
    if height:
        sector = sector.extrude(height)
    
    return sector