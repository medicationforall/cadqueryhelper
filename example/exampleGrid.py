import cadquery as cq
from cadqueryhelper import shape
from cadqueryhelper import grid

if __name__ == "__main__":
    cube = shape.cube(5,5,2)
    cylinder = shape.cylinder(2.5,2)
    cone = shape.cone()
    hexagon = shape.regular_polygon(sides=6)

    ex_grid = grid.make_grid(part=cube, dim = [6,6])
    cq.exporters.export(ex_grid,'out/grid.stl')
