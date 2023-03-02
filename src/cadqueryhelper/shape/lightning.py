import cadquery as cq

def lightning(length=25, width = 50, height = 5, x_dist = 3, y_dist=6):
    x_actual = x_dist + y_dist
    pts = [
        (0,0),# origin point
        (length, width/2+y_dist),
        (0+x_actual, width/2),
        (length, width),# top point
        (0, width/2-y_dist),
        (length-x_actual, width/2),
    ]

    shape = (
        cq.Workplane("XY")
        .polyline(pts).close()
        .extrude(height)
        .translate((-1*(length/2),-1*(width/2),-1*height/2))

    )

    return shape
