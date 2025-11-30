import cadquery as cq

def ellipse_sector(
    diameter_x:float = 20,
    diameter_y:float = 30,
    angle:float = 30,
    rotation_angle:float = 0,
    height:float = 5,
    debug:bool = False
):
    length = diameter_x/2
    width = diameter_y/2
    
    sector = (
        cq.Workplane("XY")
        .lineTo(length,0)
        .ellipseArc(
            length, 
            width, 
            0, 
            angle, 
            rotation_angle,
            startAtCurrent= True 
        )
        .close()
    )
    
    if height:
        sector = sector.extrude(height)
        
    if debug:
        outline = (
            cq.Workplane("XY")
            .ellipse(length,width, rotation_angle)
        )
        sector = sector.add(outline)
    
    return sector