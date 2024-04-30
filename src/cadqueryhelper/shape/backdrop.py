import cadquery as cq

def backdrop(
        length:float = 200, 
        width:float = 250, 
        height:float = 150,
        thickness:float = 4,
        operation:str = 'fillet',#chamfer, fillet
        operation_dist:float = 20
) -> cq.Workplane:
    box = cq.Workplane('XY').box(length, width, height)
    cut_box = cq.Workplane('XY').box(length, width, height)
    
    if operation == 'chamfer':
        box = box.faces("Y").edges("<Z").chamfer(operation_dist)
        cut_box = cut_box.faces("Y").edges("<Z").chamfer(operation_dist)
    if operation == 'fillet':
        box = box.faces("Y").edges("<Z").fillet(operation_dist)
        cut_box = cut_box.faces("Y").edges("<Z").fillet(operation_dist-thickness)
        
    scene = (
        cq.Workplane("XY")
        .union(box)
        .cut(cut_box.translate((0,-thickness,thickness)))
    )
    return scene