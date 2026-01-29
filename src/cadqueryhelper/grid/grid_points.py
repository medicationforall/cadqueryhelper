def grid_points(
    columns:int = 5,
    rows:int = 6,
    x_spacing:float = 5,
    y_spacing:float = 5
) -> tuple[list[list[tuple[float,float]]], list[tuple[float,float]]]:
    cells = rows * columns
    
    r = -1
    
    points:list[list[tuple[float,float]]]|None = None
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
        
        x_pos = x_spacing*c
        y_pos = -y_spacing*r
        
        row_points.append((x_pos,y_pos))
        raw_points.append((x_pos,y_pos))
        
    #append last row
    points.append(row_points)
    return points, raw_points