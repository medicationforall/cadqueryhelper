# Shape Documentation

## Example Usage

``` python
import cadquery as cq #main cadquery library
from cadqueryhelper import shape # The shape library this document is about

part = shape.arrow() # Generate a solid using it's default values
cq.exporters.export(part,'out/arrow.stl') # write the file to an stil file

if part.metadata:
    print(part.metadata) # print the parts bounding box
```

The code above:
* Imports the required libraries.
* Generates a solid using default setting.
* Exports the solid to a file.
* Prints the parts metadata to the console.

#### Generated Output
![](image/01.png)

Metadata / bounding box
<br />![](image/02.png)

----

## Shape Conventions
* **Length** is along the **X** axis
* **Width** is along the **Y** axis
* **Height** is along the **Z** axis
* Shapes are centered along the X, Y, and Z axis.

---

# Shapes

---

## Arrow
### Parameters
* length
* inner_length
* width
* width_outset
* height

![](image/04.png)

* [source](../src/shape/arrow.py)
* [example](../example/shape/arrow.py)
* [stl](../out/arrow.stl)


### Examples

#### Negative width_outset

``` python
part = shape.arrow(width_outset=-1)
```

![](image/05.png)

---
## Cone
### Parameters
* radius - base
* radius_top
* height

![](image/06.png)

* [source](../src/shape/cone.py)
* [example](../example/shape/cone.py)
* [stl](../out/cone.stl)

---
## Cube
### Parameters
* length
* width
* height

![](image/07.png)

* [source](../src/shape/cube.py)
* [example](../example/shape/cube.py)
* [stl](../out/cube.stl)

---
## Cylinder
### Parameters
* radius
* height

![](image/08.png)

* [source](../src/shape/cylinder.py)
* [example](../example/shape/cylinder.py)
* [stl](../out/cylinder.stl)


---
## Rail
### Parameters
* length
* width
* height
* inner_height

![](image/09.png)
<br />

* [source](../src/shape/rail.py)
* [example](../example/shape/rail.py)
* [stl](../out/rail.stl)

---
## Regular Polygon
[wikipedia](https://en.wikipedia.org/wiki/Regular_polygon)
### Parameters
* radius
* sides
* height

![](image/11.png)

* [source](../src/shape/regularPolygon.py)
* [example](../example/shape/hexagon.py)
* [stl](../out/hexagon.stl)


---
## Rhombus
### Parameters
* width
* offset
* height

![](image/10.png)

* [source](../src/shape/rhombus.py)
* [example](../example/shape/rhombus.py)
* [stl](../out/rhombus.stl)
