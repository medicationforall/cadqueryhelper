import cadquery as cq

def rotate_grid(
        shape:cq.Workplane|None = None,
        rotate_increment=-90
    ):
    rotation = 0
    count =0

    if not shape:
        raise Exception('rotate_grid: shape can not the None')

    def add_rotate(loc: cq.Location) -> cq.Shape:
        nonlocal rotation
        nonlocal count
        if count% 4 == 0:
            rotation=0
        
        shape_rotate = shape.rotate((0,0,1),(0,0,0),rotation)
        rotation+=rotate_increment
        
        count+=1
    
        return shape_rotate.val().located(loc) #type: ignore
    
    result = (
        cq.Workplane("XY")
        .rarray(
            xSpacing = 10, 
            ySpacing = 10,
            xCount = 4, 
            yCount= 4, 
            center = True)
        .eachpoint(callback = add_rotate)
    )
    return result