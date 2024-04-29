import cadquery as cq

def trapezoid(
        length:float|None = 75, 
        width:float = 25, 
        height:float = 25, 
        top_width:float = 10
    )->cq.Workplane:
    top_x:float = (width - top_width)/2
    
    points = [
        (0,0),
        (top_x,height),
        (top_x+top_width,height),
        (width,0)
    ]

    work = (
        cq.Workplane("XY").center(-(width/2),-(height/2))
        .polyline(points).close()
    )
    
    if length:
        work = work.extrude(length).translate((0,0,-(length/2))).rotate((1,0,0),(0,0,0),-90)
    return work