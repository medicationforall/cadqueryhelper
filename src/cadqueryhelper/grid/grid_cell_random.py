import cadquery as cq
from .cell_single import cell_single
import random
from numpy import arange

def _resolve_value(var:tuple[float,float,float]|float|None)->float|None:
    if type(var) is tuple:
        var_choices = arange(var[0], var[1]+var[2], var[2])
        value = random.choice(var_choices)
        return float(value)
    else:
        return var #type:ignore
        


def grid_cell_random(
    cells_collection:list[list[tuple[float,float]]],
    height:tuple[float,float,float]|float|None = (1,5,1),
    taper:tuple[float,float,float]|float|None = None,
    offset:tuple[float,float,float]|float|None= -.25,
    seed:str = "test"
)->cq.Workplane:
    pattern = cq.Workplane("XY")
    if seed:
        random.seed (seed)

    for points in cells_collection:
        h:float|None = _resolve_value(height)
        t:float|None = _resolve_value(taper)
        o:float|None = _resolve_value(offset)
        face = cell_single(points, h, t, o)
        pattern = pattern.add(face)
        
    return pattern