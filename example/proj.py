import cadquery as cq
from cadqueryhelper import parts



if __name__ == "__main__":
    print('this is main')
    #part = test.make_test_part()
    box = parts.make_cube()
    cylinder = parts.make_cylinder()
    cone = parts.make_cone()
    hexagon = parts.make_hexagon()

    workspace = cq.Workplane('XY')
    workspace.add(hexagon)

    cq.exporters.export(workspace,'out/proj2.stl')
