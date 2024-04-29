import cadquery as cq
import math

def sine(
        length:float = 60,
        width:float = 10,
        height:float = 3,
        segment_length:float = 5,
        inner_width:float = 7
    ) -> cq.Workplane:
    segment_count = math.ceil(length / segment_length)+4

    pts = [(0,0),(width,0)]
    spline_pts = []
    x = width
    y = 0

    for i in range(segment_count):
        y = segment_length + (segment_length*i)

        if i%2 ==0:

            x = inner_width
        else:
            x = width
        spline_pts.append((x,y))

    result = (
        cq.Workplane("XY")
        .polyline(pts)
        .spline(spline_pts, includeCurrent=True)
        .lineTo(0,y)
        .close()
    )

    if height:
        result = result.extrude(height)

        result = (
            result
            .translate(((-1*width/2),(-1*(segment_count*segment_length)/2),-1*height/2))
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
            .translate(((-1*width/2),-1*length/2,-1*height/2))
            .rotate((0,0,1),(0,0,0),90)
            .rotate((1,0,0),(0,0,0),180)
        )
        return result
