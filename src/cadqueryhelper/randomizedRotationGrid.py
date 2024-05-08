import cadquery as cq
import random
from typing import Callable

def randomized_rotation_grid(
        shape:cq.Workplane|None = None, 
        seed:str = "test",
        rotate_increment:int = 90, 
        rotate_min:int = 0, 
        rotate_max:int = 360,
        x_count:int = 5,
        y_count:int = 5,
        x_spacing:float = 10,
        y_spacing:float = 10
    ) -> cq.Workplane:
    random.seed(seed)
    if not shape:
        raise Exception("Missing shape")
    
    def add_rotate(loc:cq.Location) -> cq.Shape:
        rotation = random.randrange(rotate_min, rotate_max, rotate_increment)
        shape_rotate = shape.rotate((0,0,1),(0,0,0),rotation)
        return shape_rotate.val().located(loc) #type:ignore
    
    result = (
        cq.Workplane("XY")
        .rarray(
            xSpacing = x_spacing, 
            ySpacing = y_spacing,
            xCount = x_count, 
            yCount= y_count, 
            center = True)
        .eachpoint(callback = add_rotate)
    )
    return result