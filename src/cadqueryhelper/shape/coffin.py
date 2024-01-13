import cadquery as cq

def coffin(
    length = 30, # length between the two mid points
    width = 36, # distance between the top and base
    height = 10, # extruded height of the face, can be falsy
    top_length = 20, # length of the top
    base_length = 20, # length of the base
    mid_offset = 5 # middle points distance from the width center. Can be positive or negative.
):
    top_offset = (length - top_length) / 2
    mid_offset = (width/2) + mid_offset
    base_offset = (length - base_length) / 2

    pts = [
        (base_offset,0), # base left
        (length-base_offset,0), # base right 
        (length, mid_offset), # mid right
        (length-top_offset, width), # top right
        (top_offset, width), # top left
        (0, mid_offset) # mid left
    ]

    lines = cq.Workplane("XY").polyline(pts).close()
        
    if height:
        lines = lines.extrude(height).translate((0,0,-1*(height/2)))

    #center along the length and width    
    lines = lines.translate((-1*(length/2),-1*(width/2),0))
        
    return lines