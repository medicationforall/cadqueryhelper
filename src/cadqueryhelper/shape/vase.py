import cadquery as cq

def vase(
        shape:cq.Workplane, 
        workplane_axis:str = "YZ", #'XY', 'YZ', 'XZ'
        radius:float = 1, 
        angle:float = 0, 
        rotation_angle:float = 0
    ) -> cq.Workplane:
    '''
    Assumed the shape is centered on the XY plane.
    '''
    path = (
        cq.Workplane(workplane_axis)
        .center(0,0)
        .ellipseArc(
            radius,
            radius,
            angle,
            rotation_angle = rotation_angle
        )
    )
    sweep = shape.sweep(path).translate((radius,0,0))
    return sweep
