import cadquery as cq
import math

def square(
        length = 60,
        width = 10,
        height=3,
        segment_length=5,
        inner_width = 7

    ):
    segment_count = math.ceil(length / segment_length)

    pts = [(0,0),(width,0)]
    x = width
    y = 0

    for i in range(segment_count):
        y = segment_length + (segment_length*i)

        if i % 2 == 0:
            #even
            pts.append((width,y))
            pts.append((inner_width,y))

        else:
            #odd
            pts.append((inner_width,y))
            pts.append((width,y))

    pts.append((0,y))
    result = cq.Workplane("XY").polyline(pts).close()

    if height:
        result = result.extrude(height)

        result = (
            result
            .translate((-1*width/2,-1*length/2,-1*height/2))
            .rotate((0,0,1),(0,0,0),90)
            .rotate((1,0,0),(0,0,0),180)
        )

        outline = cq.Workplane("XY").box(length, width, height)
        scene = (
            cq.Workplane("XY")
            .add(outline)
            .intersect(result)
        )

        return scene
    else:
        result = (
            result
            .translate((-1*width/2,-1*length/2,-1*height/2))
            .rotate((0,0,1),(0,0,0),90)
            .rotate((1,0,0),(0,0,0),180)
        )
        return result
