import cadquery as cq

def arrow(length=10, inner_length=5, width=5, width_outset=2, height=3):
    points = [
        (0,0),
        (0,width),
        (inner_length, width),
        (inner_length, width+width_outset),
        (length, width/2),
        (inner_length, 0-width_outset),
        (inner_length, 0),
        ]
    work = cq.Workplane().center(0,0).polyline(points).close().extrude(height)

    #todo need to address width when outset is positive
    meta = {'type':'arrow','height':height, 'length':length, 'width':width}
    work.metadata = meta
    return work
