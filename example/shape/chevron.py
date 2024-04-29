import cadquery as cq
from cadqueryhelper import shape

result = shape.chevron(
    length=10, 
    width=7, 
    height=2, 
    inner_width=3, 
    alt=False
)

#show_object(result)
cq.exporters.export(result,'stl/shape_chevron.stl')

alt = shape.chevron(
    length=10, 
    width=7, 
    height=2, 
    inner_width=3, 
    alt=True
)

#show_object(alt)
cq.exporters.export(alt,'stl/shape_chevron_alt.stl')
