import cadquery as cq
from cadqueryhelper.shape import pipe

test_shape = cq.Workplane('XY').rect(4,8)
pst = pts = [(0,0), (20,-20), (50,-20), (50,-30)]
result = pipe(test_shape, pts)

#show_object(result)
cq.exporters.export(result,'stl/shape_pipe.stl')

