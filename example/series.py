import cadquery as cq
from cadqueryhelper import shape
from cadqueryhelper import series

if __name__ == "__main__":
    star = shape.star()
    box = cq.Workplane().box(1,2,3)

    st_series = series(shape = box, length_offset=None, width_offset=1, height_offset=None, size=4)
    cq.exporters.export(st_series,'out/series.stl')

    if st_series.metadata:
        print(st_series.metadata)
