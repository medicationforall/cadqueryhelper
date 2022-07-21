import cadquery as cq
from cadqueryhelper import parts
from cadqueryhelper import grid

if __name__ == "__main__":
    hexagon = parts.make_hexagon().rotate((0,0,1),(0,0,0), 30)

    ex_grid = grid.make_grid(part = hexagon, dim = [9.5,8], odd_col_push = [4.7,0])
    #comp = ex_grid.toCompound()
    cq.exporters.export(ex_grid,'out/hexgrid.stl')
