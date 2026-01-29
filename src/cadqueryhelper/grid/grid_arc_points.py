import math

def rotate_point(point:tuple[float,float], angle:float=0, origin = (0,0)):

    o_x, o_y = origin
    p_x, p_y = point
    angle = -math.radians(angle)

    q_x = o_x + math.cos(angle) * (p_x - o_x) - math.sin(angle) * (p_y - o_y)
    q_y = o_y + math.sin(angle) * (p_x - o_x) + math.cos(angle) * (p_y - o_y)
    
    return (q_x, q_y)

def make_arc_row_points(radius:float, count:int = 4, angle:float = 90):
    points = []
    last = (radius, 0)
    
    rotate_degrees = angle / (count-1)
    rotate = rotate_degrees*(count-1)
    coord = rotate_point((radius,0), rotate)
    points.append(coord)

    r_points = [] 
    
    for i in range(1,count-1,1):
        rotate = rotate_degrees*i
        coord = rotate_point((radius,0), rotate)
        r_points.append(coord)
    r_points.reverse()
    points = points + r_points
    points.append(last)
    
    return points

def grid_arc_points(
    columns:int = 10,
    rows:int = 8,
    x_spacing:float = 10,
    angle:float = 90,
    row_increment:int = 0
) -> tuple[list[list[tuple[float,float]]], list[tuple[float,float]]]:
    ring_data = []
    ring_stream = []
    for i in range(columns+1):
        #log(f'row {i}')
        if i:
            #log(f'circle {i}')
            radius = i*x_spacing
            row_count = rows + (row_increment * (i-1))
            ring_point = make_arc_row_points(radius, row_count, angle)
            ring_data.append(ring_point)
            ring_stream = ring_stream + ring_point
        else:
            pass
            #log(f'skip {i}')
                
    return ring_data, ring_stream