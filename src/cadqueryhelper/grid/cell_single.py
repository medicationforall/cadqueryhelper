import cadquery as cq

def cell_single(
    points:list[tuple[float,float]],
    height:float|None=1,
    taper:float|None=None,
    offset:float|None=-.25
) -> cq.Workplane:
    face = (
        cq.Workplane("XY")
        .polyline(points)
        .close()
    )

    if offset:
        face = face.offset2D(offset)

    if height:
        face = face.extrude(height,taper=taper)
    return face