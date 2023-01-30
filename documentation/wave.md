# Wave Documentation

---

## Conventions
* **Length** is along the **X** axis
* **Width** is along the **Y** axis
* **Height** is along the **Z** axis
* Waves are centered along the X, Y, and Z axis.

---

## Triangle

### Parameters
* length
* width
* height
* segment_length
* inner_width

``` python
result = pattern.triangle(
  length=80,
  width=20,
  height=3,
  segment_length=5,
  inner_width=5
)
```

![](image/wave/02.png)<br />

* [source](../src/cadqueryhelper/wave/triangle.py)
* [example](../example/wave/triangle.py)
* [stl](../out/wave_triangle.stl)

### Zero height

``` python
result = pattern.triangle(
  length=80,
  width=20,
  height=0,
  segment_length=5,
  inner_width=5
)
```
Returns the line segment for further operations.
![](image/wave/03.png)<br />

---
## Sawtooth

### Parameters
* length
* width
* height
* segment_length
* inner_width

``` python
result = wave.sawtooth(
    length=80,
    width=20,
    height=3,
    segment_length=15,
    inner_width=5
)
```

![](image/wave/04.png)<br />

* [source](../src/cadqueryhelper/wave/sawtooth.py)
* [example](../example/wave/sawtooth.py)
* [stl](../out/wave_sawtooth.stl)

### Zero height

``` python
result = pattern.triangle(
  length=80,
  width=20,
  height=0,
  segment_length=5,
  inner_width=5
)
```
Returns the line segment for further operations.
![](image/wave/05.png)<br />

---

## square
* length
* width
* height
* segment_length
* inner_width

``` python
result = wave.square(
    length=75.5,
    width=10,
    height=3,
    segment_length=5,
    inner_width=5
)
```

![](image/wave/06.png)<br />

* [source](../src/cadqueryhelper/wave/square.py)
* [example](../example/wave/square.py)
* [stl](../out/wave_square.stl)

### Zero height & sweep

``` python
pipe_path = cq.Workplane("XZ").spline([(0,0), (20,-20), (50,-20), (50,-30)])
result = result = wave.square(
    length=75.5,
    width=10,
    height=0,
    segment_length=5,
    inner_width=5
).sweep(pipe_path, multisection=0, isFrenet=False, clean=False)
```

![](image/wave/07.png)<br />
