import cadquery as cq

def make_circular_points(radius = 150, startAngle=0, count = 15):
    coords = []
    def add_point(loc):
        test = cq.Workplane("XY").box(10,10,10)
        coord_loc = loc.toTuple()[0]
        coords.append((coord_loc[0],coord_loc[1]))
        return test.val().located(loc)
        
    point_arc =(
        cq.Workplane("XY")
        .polarArray(
            radius  = radius, 
            startAngle = startAngle, 
            angle = 360, 
            count = count,
            fill = True,
            rotate = False
        )
        .eachpoint(callback = add_point)
    )
    return point_arc, coords

def interweave_lists(lists):
    main_list = []
    for list in lists:
        main_list = main_list + list
        
    # interse the lists
    lists_count = len(lists)
    for index, list in enumerate(lists):
        if index == 0:
            main_list[::lists_count] = list
        else:
            main_list[index::lists_count] = list
    return main_list
            

def pinwheel(count = 10, height = 3, ring_params = [{"radius": 150, "start_angle":0}, {"radius":100,"start_angle":40}]):
    point_lists = []
    
    for ring_param in ring_params:
        arc, tuple_points = make_circular_points(radius = ring_param["radius"], startAngle=ring_param["start_angle"], count = count)
        point_lists.append(tuple_points)
    
    points = interweave_lists(point_lists)

    result = cq.Workplane("XY").polyline(points).close()
    
    if height:
        return result.extrude(height).translate((0,0,-1*(height/2)))
    else:
        return result