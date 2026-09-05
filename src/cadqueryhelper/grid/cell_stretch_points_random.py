from cadqueryhelper.grid import grid_points, grid_cell_basic
import random
from numpy import arange

def _nav_cell(
    points:list[list[tuple[float,float]]], 
    x:int, 
    y:int, 
    x_stretch:int, 
    y_stretch:int
):
    l_points = []
    # x+ side
    for i in range(x_stretch+1):
        point = points[0+y][i+x]
        l_points.append(point)

    # y+ side
    x_plus_end = x_stretch+x
    for i in range(y_stretch+1):
        if i: # skip 0 index
            point = points[i+y][x_plus_end]
            l_points.append(point)

    # x- side
    y_plus_end = y_stretch+y
    for i in reversed(range(x_stretch+1)):
        if i  != x_stretch:
            point = points[y_plus_end][i+x]
            l_points.append(point)

    # y- side 
    for i in reversed(range(y_stretch+1)):
        if i and i != y_stretch:
            point = points[i+y][0+x]
            l_points.append(point)
    
    return l_points

def _resolve_value(var:tuple[float,float,float]|float|None)->float|None:
    if type(var) is tuple:
        var_choices = arange(var[0], var[1]+var[2], var[2])
        value = random.choice(var_choices)
        return float(value)
    else:
        return var #type:ignore


def cell_stretch_points_random(
        points:list[list[tuple[float,float]]],
        x_stretch:tuple[int,int,int] = (1,1,1), # min, max, step
        y_stretch:tuple[int,int,int] = (1,1,1), # min, max, step
        seed:str = "test",
        uniform_split:bool = True
    )->list[list[tuple[float,float]]]:
    if seed:
        random.seed (seed)

    cells = []
    
    accrued_length = 0
    length = len(points[0])
    width = len(points)
    break_width_count = 0
    
    while accrued_length < length-1:
        accrued_width = 0
        i_length = int(_resolve_value(x_stretch))
        
        if accrued_length + i_length >= length-1:
            #log("length override")
            i_length = length - accrued_length-1
            
        #break_count+=1
        
         
        while accrued_width < width-1:
            i_width = int(_resolve_value(y_stretch))
            
            
            if (accrued_width) + i_width > width-1:
                #log("**********width override")
                i_width = width - accrued_width-1
            #else:
                #log(f"i_width is fine {accrued_width + i_width} {width}")
            
            
            #log(f'{i_length=}, {i_width=}')
            #log(f'{accrued_length=}, {accrued_width=}')
            should_split = int(_resolve_value((0,1,1)))
            if uniform_split and i_length > 1 and should_split:
                #log(f'attempt uniform split {i_length}')
                split_point = int(_resolve_value((1,i_length-1,1)))
                diff = i_length - split_point
                #log(f'{split_point}, {diff=}')
                
                begin_split_cell = _nav_cell(points, accrued_length, accrued_width, split_point, i_width)
                cells.append(begin_split_cell)
                
                end_split_cell = _nav_cell(points, accrued_length+split_point, accrued_width, diff, i_width)
                cells.append(end_split_cell)
                
            else:
                try:
                    l_points = _nav_cell(points, accrued_length, accrued_width, i_length, i_width)
                    cells.append(l_points)
                except:
                    print(f'{i_length=}, {i_width=}')
                    print(f'{accrued_length=}, {accrued_width=}')
                    print("something went awry")
                
            break_width_count+=1
            accrued_width += i_width
            
        accrued_length += i_length


    return cells