import cadquery as cq
from cadqueryhelper import parts
from cadqueryhelper import grid

if __name__ == "__main__":
    #print('this is the grid running as main')
    cube = parts.make_cube(5,5,2)
    cylinder = parts.make_cylinder(2.5,2)
    cone = parts.make_cone()
    hexagon = parts.make_hexagon()


    ex_grid = grid.make_grid(part=cube, dim = [6,6])
    comp = ex_grid.toCompound()
    cq.exporters.export(comp,'out/grid.stl')
