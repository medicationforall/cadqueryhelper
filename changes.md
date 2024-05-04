# cadqueryhelper Changelog

## main wip

## 1.0.0
* This release has "breaking" changes.
* Added type annotations.
* Removed setting meta attributes on Workplane objects (breaking change if you utilized this).
* Update documentation shape coffin image.
* Removed *old* denoted examples.
* renamed out directory to stl to be more in line with other project structures.
* Added Trapezoid shape.
* Added example_runner.py which runs all of the example scripts in one place
* Modified the random function is used for calculating variable height with the irregular grid. The new functions supports better type safety for floats as opposed to implicit casting to integers but the generated outputs are now different from previous versions of the library.
* Regenerated all of the examples.
* Added backdrop shape, example, stl, and documentation
* Yoinked Jersey Barrier code from cqindustry and added it to the shapes.
* Added license blocks
* Formalized the pipe shape and added parameters.
* Added vase shape and example / documentation
* Added HelperPlate
* Updated README.md


## 0.2.1
* Added shape.coffin
  * Example
  * Documentation
  * out/stl

## 0.2.0
* Make Base class compatible with the "with" keyword.
* remove irregular grid log reference.

## 0.1.6
* Added pinwheel shape

## 0.1.5
* Union ibeam shape
* Added corner_join shape
  * example
  * documentation
* Added hinge documentation
* Added hinge documentation link to README.md

## 0.1.4
* Add Base class
* Added Hinge Class
* Added hinge example "python ./example/hinge.py"

## 0.1.3
* Refactored regular polygon code.

## 0.1.2
* Irregular grid added support to hardcode cell items.
* Updated the license
* upped CadQuery version

## 0.1.1
* Built out wave documentation
* Added lightning basic shape
* Added Irregular Grid
  * initial documentation

## 0.1.0
* center round arch
* Added arch round
* Added wave triangle
* Added wave sawtooth
* Added wave square
* Added rough sine wave
* Fix arrow center
  * 0 height returns line path
* Chevron 0 height returns line path
* Diamond 0 height returns line path
* Rail 0 width returns line path
* arch_pointed 0 width returns line path
* regular_polygon 0 height returns line path
* Star 0 height returns line path

## 0.0.8
* Updated cadquery version

## 0.0.7
* Added Diamond, and Chevron shape
  * With example
* Series now has support for providing an operation callback which is applied with each iteration of the loop.
  * added series operation example
* Updated documentation
  * Shapes
  * Series
  * Grid
* Specified cqmore version dependency
* cleaned up star grid example

## 0.0.6
* Initial Release
