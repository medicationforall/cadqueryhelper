import cadquery as cq

def grid_cell_basic(
    cells_collection,
    height:float=1,
    taper=None
)->cq.Workplane:
    pattern = cq.Workplane("XY")
    
    for points in cells_collection:
        face = cq.Workplane("XY").polyline(points).close().extrude(height,taper=taper)
        pattern = pattern.add(face)
        
    return pattern