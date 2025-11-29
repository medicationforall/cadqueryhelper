# cadqueryhelper Changelog

## main wip

## 1.7.2
* Cleaned up the shape code
  * Removed unused variables
  * Added license blocks
* Cleanup shape documentation
  * Added deprecation notices
  * Annotated step_pyramid example picture
  * Annotated teardrop example picture
* Added shape 
  * crescent

## 1.7.1
* Added shape step_pyramid

## 1.7.0
* Upgraded to cadquery version 2.6.1
* Added shape teardrop

## 1.6.0
* Added ring shape.
* Cleaned up shape documentation
  * built out examples
  * Removed deprecated references to metadata
  * Added an index
  * Built out vase examples

## 1.5.1
* Changed from using assembly.save (deprecated) to assembly.export
* Added example helper_plate to the example_runner

## 1.5.0
* Updated dependecies in pyproject.toml
  * Updated min python version to 3.10 
  * Updated cadquery version 2.5.2
  * Removed nlopt specific version.
  * Removed numpy specific version.
* Cleaned up page links in project.urls in pyproject.toml
* Cleaned up instances where I was setting the callback parameter for workplane.eachpoint invocations.
  * https://github.com/CadQuery/cadquery/issues/1395  

## 1.4.2
* Make seed property nullable for Irregular Grid and Randomized Rotation Grid

## 1.4.1
* Added license blocks

## 1.4.0
* Added mising wave.sine source, example, stl links.
* Added wave uneven_spline and example.
* Added wave uneven_spline_grid example.
* Updated wave documentation.
* Fix uneven_grid stl name typo.

## 1.3.0
* Set hard coded dependencies for nlopt, numpy and cadquery

## 1.2.5
* Fix a bug with uneven wave

## 1.2.4
* Added uneven wave
  * Included two examples
* Updated wave documentation

## 1.2.3
* Upped cadquery version to 2.4.x

## 1.2.2
* Fixed a bug where I had changed the behavior of the hinge when I refactor.
  * the receiver and the driver were switched which had the knock effect of modifying existing projects in unexpected ways.
  * It wasn't tehnically wrong just different.
  * I added a new flag called invert which toggles the behavior of the driver and receiver.
  * Addded hinge example hinge_invert.py
  * Updated hinge documentation 

## 1.2.1
* Added additional parameters to Hinge
  * render - accepts 'driver', 'receiver', or 'both'
  * The value of render determines which parts of the hinge will be rendered.
  * Addded hinge example hinge_render.py
  * Updated hinge documentation

## 1.2.0
* Added additional parameters to Hinge
    * tab_height
    * tab_z_translate
* Added hinge example hinge_larger_tab.py
* Updated hinge documentation

## 1.1.2
* Added rotate_grid

## 1.1.1
* Refactored series to center ouput again
  * No longer relies on assembly 

## 1.1.0
* Added randomized_rotation_grid
* add scheme_grid

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
