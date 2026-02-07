import cadquery as cq
from .cell_single import cell_single

def grid_cell_basic(
    cells_collection:list[list[tuple[float,float]]],
    height:float|None=1,
    taper:float|None=None,
    offset:float|None=None
)->cq.Workplane:
    pattern = cq.Workplane("XY")
    
    for points in cells_collection:
        face = cell_single(points, height, taper, offset)
        pattern = pattern.add(face)
        
    return pattern