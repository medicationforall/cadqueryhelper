
def _nav_cell(
    points, 
    x, 
    y, 
    x_stretch, 
    y_stretch
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


def cell_stretch_points(
        points,
        x_stretch:int = 1,
        y_stretch:int = 1
    ):

    if x_stretch < len(points[0])  :
        length = len(points[0]) - x_stretch
    else:
        raise Exception(f'x_stretch {x_stretch} can not be greater than points x length {len(points[0])}')

    if y_stretch < len(points):
        width = len(points) - y_stretch
    else:
        raise Exception(f'y_stretch {y_stretch} can not be greater than points y length {len(points)}')
    
    cells = []
    
    for y in range(0, width, y_stretch):
        for x in range(0, length, x_stretch):
            l_points = _nav_cell(points, x, y, x_stretch, y_stretch)
            cells.append(l_points)

    return cells