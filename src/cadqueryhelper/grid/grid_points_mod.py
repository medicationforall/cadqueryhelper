def grid_points_mod(
    columns:int = 5,
    rows:int = 6,
    x_spacing:float|list[float]= [5,10],
    y_spacing:float|list[float] = 5,
    row_x_mod:list[int] = [0,1],
    row_x_offset:list[float] = [0,-2.5]
) -> tuple[list[list[tuple[float,float]]], list[tuple[float,float]]]:
    cells = rows * columns
    
    r = -1
    
    points:list[list[tuple[float,float]]]|None = None
    row_points = []
    raw_points = []
    
    
    previous_x = 0
    previous_y = 0
    row_mod = row_x_mod[0]
    row_offset = row_x_offset[0]
    
    if type(x_spacing) is list:
        previous_x = -x_spacing[0] + row_offset
        
    if type(y_spacing) is list:
        previous_y = -y_spacing[0]
    
    for i in range(cells):
        c = i % columns
        
        if c == 0:
            r += 1
            
            if type(y_spacing) is list:
                y_index = r % len(y_spacing)
                previous_y = previous_y + y_spacing[y_index]
            
            if points is not None:
                points.append(row_points)
                row_points = []
                
                row_mod_index = r % len(row_x_mod)
                row_mod = row_x_mod[row_mod_index]
                
                row_offset_index = r % len(row_x_offset)
                row_offset = row_x_offset[row_offset_index]

                if type(x_spacing) is list:
                   previous_x = -x_spacing[0] + row_offset
                   
                 
            else:
                points = []

        # x position
        if type(x_spacing) is list:
            #log(f'{x_spacing} {len(x_spacing)} {i}')
            x_index = c % len(x_spacing)
            x_index += row_mod

            x_pos = previous_x + x_spacing[x_index % len(x_spacing)]
            #log(f'{x_pos}')
        else:
            x_pos = x_spacing*c
            
        # y position
        if type(y_spacing) is list:
            #y_index = r % len(y_spacing)
            #y_pos = previous_y + y_spacing[y_index]
            
            y_pos = -previous_y
        else:
            y_pos = -y_spacing*r
        
        row_points.append((x_pos,y_pos))
        raw_points.append((x_pos,y_pos))
        previous_x = x_pos
        
    #append last row
    points.append(row_points)
    return points, raw_points