def join_cells_interlock(
        points:list[list[tuple[float,float]]],
        cells:list[list[tuple[float,float]]],
        start:int = 1,
        top_end_index:int = 3,
        bottom_start_index:int = 2,
        top_cap_index:int = 3
    ):
    mod_cells = []
    length = len(cells)
    col_length = len(points[0])
    
    for i in range(start,len(cells),2):
        b_index = i + (col_length-1)
        
        if b_index < length:
            top = cells[i]
            bottom = cells[b_index]
    
            new_cell = top[:top_end_index] + bottom[bottom_start_index:] + top[top_cap_index:]
            mod_cells.append(new_cell)
        else:
            break
        
    return mod_cells