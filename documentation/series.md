# Series Documentation

## Series
### Parameters
* shape
* size
* length_offset
* width_offset
* height_offset

simple loop that repeats the given shape n-number of times based on the *size* parameter.

### Examples

#### Star series repeated over the y-axis
``` python
import cadquery as cq
from cadqueryhelper import shape
from cadqueryhelper import series

if __name__ == "__main__":
    star = shape.star()

    st_series = series.make_series(shape = star, length_offset=None, width_offset=-11, height_offset=0, size=4)
    cq.exporters.export(st_series,'out/series.stl')

    if st_series.metadata:
        print(st_series.metadata)
```


![](image/series/01.png)

#### Star series repeated over the y and z-axis
``` python
  series.make_series(shape = star, length_offset=None, width_offset=-11, height_offset=0, size=4)
```
![](image/series/02.png)

#### Star series repeated over the x, y and z-axis
``` python
  series.make_series(shape = star, length_offset=1, width_offset=-11, height_offset=0, size=3)
```
![](image/series/03.png)


* [source](../src/cadqueryhelper/series.py)
* [example](../example/series.py)
* [stl](../out/series.stl)
