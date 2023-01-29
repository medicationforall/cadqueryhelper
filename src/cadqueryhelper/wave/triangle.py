import cadquery as cq
import math

def triangle(
        length = 60,
        width = 10,
        height=3,
        segment_length=5,
        inner_width = 7
    ):
    segment_count = math.floor(length / segment_length)

    pts = [(0,0),(inner_width,0)]
    x = width
    y = 0

    for i in range(segment_count):
        y = segment_length + (segment_length*i)

        if i%2 ==0:
            x = width
        else:
            x = inner_width
        pts.append((x,y))

    pts.append((0,y))
    result = cq.Workplane("XY").polyline(pts).close()

    return (
        result.extrude(height)
        .translate((-1*width/2,-1*length/2,-1*height/2))
        .rotate((0,0,1),(0,0,0),90)
        .rotate((1,0,0),(0,0,0),180)
    )
