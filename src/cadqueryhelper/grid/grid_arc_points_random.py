from .grid_arc_points import rotate_point
import random
from numpy import arange

def make_arc_row_points_random(
        radius:float, 
        length_modifiers,
        width_modifiers,
        count:int = 4, 
        angle:float = 90,
        seed:str|None='test'
    ):
    points = []

    if seed:
        random.seed(seed)
    
    rotate_degrees = angle / (count-1)
    rotate = rotate_degrees*(count-1)
    
    #first point
    coord = rotate_point((radius,0), rotate)
    x_mod = random.choice(length_modifiers)
    y_mod = random.choice(width_modifiers)
    mod_coord = (coord[0]+x_mod,coord[1]+y_mod)
    points.append(mod_coord)

    r_points = [] 
    
    for i in range(1,count-1,1):
        rotate = rotate_degrees*i
        coord = rotate_point((radius,0), rotate)

        x_mod = random.choice(length_modifiers)
        y_mod = random.choice(width_modifiers)
        
        mod_coord = (coord[0]+x_mod,coord[1]+y_mod)

        r_points.append(mod_coord)
    r_points.reverse()
    points = points + r_points
    
    #last points
    last_coord = (radius, 0)
    x_mod = random.choice(length_modifiers)
    y_mod = random.choice(width_modifiers)
    mod_coord_last = (last_coord[0]+x_mod,last_coord[1]+y_mod)
    points.append(mod_coord_last)
    
    return points

def grid_arc_points_random(
    columns:int = 10,
    rows:int = 8,
    x_spacing:float = 10,
    angle:float = 90,
    row_increment:int = 0,
    shift_x:tuple[float, float, float] = (-2, 5, 1),#min max step
    shift_y:tuple[float, float, float] = (-3, 5, .5),#min max step
    seed:str|None = 'test'
) -> tuple[list[list[tuple[float,float]]], list[tuple[float,float]]]:
    ring_data = []
    ring_stream = []

    if seed:
        random.seed(seed)

    length_modifiers = arange(shift_x[0],shift_x[1]+shift_x[2], shift_x[2])
    width_modifiers = arange(shift_y[0],shift_y[1]+shift_y[2], shift_y[2])

    for i in range(columns+1):
        #log(f'row {i}')
        if i:
            #log(f'circle {i}')
            radius = i*x_spacing
            row_count = rows + (row_increment * (i-1))
            ring_point = make_arc_row_points_random(
                radius,
                length_modifiers,
                width_modifiers, 
                row_count, 
                angle,
                f"{seed}_{i}"
            )
            ring_data.append(ring_point)
            ring_stream = ring_stream + ring_point
        else:
            pass
            #log(f'skip {i}')
                
    return ring_data, ring_stream