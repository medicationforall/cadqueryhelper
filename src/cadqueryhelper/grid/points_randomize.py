import random
from numpy import arange
from typing import Tuple

def points_randomize(
    points:list[list[tuple[float,float]]],
    shift_x:tuple[float,float,float] = (-2,2,1),
    shift_y:tuple[float,float,float] = (-2,2,1),
    seed:str = 'test'
) -> tuple[list[list[tuple[float,float]]], list[tuple[float,float]]]:
    r_points = []
    stream = []
    length_modifiers = arange(shift_x[0],shift_x[1]+shift_x[2], shift_x[2])
    width_modifiers = arange(shift_y[0],shift_y[1]+shift_y[2], shift_y[2])
    
    if seed:
        random.seed(seed)
    
    for r_i,r in enumerate(points):
        row = []
        for c_i,c in enumerate(r):
            x_mod = random.choice(length_modifiers)
            y_mod = random.choice(width_modifiers)
            ref_point = points[r_i][c_i]
            new_x = ref_point[0] + x_mod
            new_y = ref_point[1] + y_mod
            
            new_point = (new_x,new_y)
            row.append(new_point)
            stream.append(new_point)
        r_points.append(row)
        
    return r_points, stream