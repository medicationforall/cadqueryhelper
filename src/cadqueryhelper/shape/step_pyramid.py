import cadquery as cq

def step_pyramid(
    length:float = 40,
    width:float = 60,
    height:float = 30,
    steps:int = 3,
    min_length:float = 10,
    min_width:float = 15,
    ellipse:bool =  False
):
    pyramid = cq.Workplane("XY")
    l_height = height/steps
    length_step = (length-min_length)/(steps-1)
    width_step = (width-min_width)/(steps-1)
    total_height = 0

    for i in range(steps):
        l_length = length - length_step*i
        l_width = width - width_step*i

        if ellipse:
            sk = cq.Sketch().ellipse(l_length,l_width)
            layer = (
                cq.Workplane("XY")
                .placeSketch(sk)
                .wire()
                .extrude(l_height)
            )
        else:
            layer = cq.Workplane("XY").box(
                l_length,
                l_width,
                l_height
            ).translate((0,0,l_height/2))
        
        pyramid = pyramid.union(layer.translate((0,0,total_height)))
        total_height+=l_height
        
    return pyramid