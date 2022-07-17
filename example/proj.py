import cadquery as cq
import test
import parts



if __name__ == "__main__":
    print('this is main')
    #part = test.make_test_part()
    box = parts.make_cube()
    cylinder = parts.make_cylinder()
    cone = parts.make_cone()

    workspace = cq.Workplane('XY')
    workspace.add(cone)

    #assembly = cq.Assembly()
    #assembly.add(box, name="cone0")
    #assembly.add(box, name="cone1")
    #assembly.constrain("cone0@faces@<Z", "cone1@faces@<Z", "Axis")
    #assembly.solve()

    #comp = assembly.toCompound()

    cq.exporters.export(workspace,'out/proj2.stl')
