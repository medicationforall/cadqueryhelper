import cadquery as cq
from cadqueryhelper import shape
from cadqueryhelper import series

star = shape.star()
box = cq.Workplane().box(1,2,3)

st_series = series(
    shape = box, 
    length_offset=None, 
    width_offset=1, 
    height_offset=None, 
    size=4,
    union=False
)

#show_object(st_series)
cq.exporters.export(st_series,'stl/series.stl')
