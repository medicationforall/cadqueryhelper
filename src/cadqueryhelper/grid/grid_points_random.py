import random
from numpy import arange

def grid_points_random(
    columns:int = 5,
    rows:int = 6,
    x_spacing :float = 10,
    y_spacing:float = 10,
    shift_x:tuple[float, float, float] = (-2, 5, 1),#min max step
    shift_y:tuple[float, float, float] = (-3, 5, .5),#min max step
    seed:str|None = 'test'
) -> tuple[list[list[tuple[float,float]]], list[tuple[float,float]]]:
    
    cells = rows * columns

    if seed:
        random.seed(seed)
    length_modifiers = arange(shift_x[0],shift_x[1]+shift_x[2], shift_x[2])
    width_modifiers = arange(shift_y[0],shift_y[1]+shift_y[2], shift_y[2])
    r = -1
    
    points = None
    row_points = []
    raw_points = []
    
    for i in range(cells):
        c = i % columns
        
        if c == 0:
            r += 1
            if points is not None:
                points.append(row_points)
                row_points = []
            else:
                points = []
        x_mod = random.choice(length_modifiers)
        x_pos = (x_spacing*c)+x_mod
        y_mod = random.choice(width_modifiers)
        y_pos = (-y_spacing*r)+y_mod
        
        row_points.append((float(x_pos),float(y_pos)))
        raw_points.append((float(x_pos),float(y_pos)))
        
    #last row
    points.append(row_points)
    return points,raw_points