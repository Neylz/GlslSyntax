# GLSLSyntax

This is a Python package that provides the syntax and objects to manipulate vectors and matrices like in GLSL.

## Installation

```bash
pip install glslsyntax
```

## Usage

Import everything to get the closest experience to GLSL.
```python
from glslsyntax import *
```

You can also import only vectors or matrices.
```python
from glslsyntax.vectors import *
from glslsyntax.matrices import *
```

## Features

### Vectors

#### Declaration
Vectors support integer and float values. They can be declared by typing `vec` followed by the number of dimensions. Up to 4 dimensions are supported. To declare the vector, you can pass the values as arguments or a single value to create a vector with all dimensions set to that value.
```python
# Classic declaration
2Dvec = vec2(1, 2.3)
3Dvec = vec3(1, 2, 3)
4Dvec = vec4(1, 2, 3, 4)

# Shorthand declaration
2Dvec2 = vec2(1) # (1, 1)
3Dvec2 = vec3(1.1) # (1.1, 1.1, 1.1)
4Dvec2 = vec4(1) # (1, 1, 1, 1)
```

You can also use other vectors to create a new one.
```python
4Dvec3 = vec4(vec2(1), vec2(3, 4)) # (1, 1, 3, 4)
3Dvec3 = vec3(1, vec2(2, 3.5)) # (1, 2, 3.5)
```

#### Attributes

All vectors have the following attributes:
- `x`, `y`, `z`, `w` to access the components of the vector. `x` and `y` are always available, `z` is available for 3D and 4D vectors, and `w` is available for 4D vectors.
- `r`, `g`, `b`, `a` are aliases for `x`, `y`, `z`, `w` and acts in the same way.
- `magnitude` to get the magnitude of the vector.
- `normal` to get the normalized vector. This doesn't modify the original vector.
- `size` to get the number of dimensions of the vector.

The `x`, `y`, `z`, `w` attributes can be used together to create a new vector with a number of dimensions equal to the number of attributes used. The order of the attributes will affect the order of the components in the new vector.
```python
vec = vec3(1, 2, 3)

vec_2 = vec.yzx # vec3(2, 3, 1)
vec_3 = vec.zzz # vec3(3, 3, 3)

print(vec.magnitude) # 3.7416573867739413
print(vec.normal.x) # 0.2672612419124244
print(vec.xz.size) # 2
```


The `x`, `y`, `z`, `w` attributes can be used to set the components of the vector.

```python
vec = vec3(1, 2, 3)
vec.x = 4

print(vec) # vec3(4, 2, 3)
```

#### Methods

Some functions of GLSL have been implemented as methods of the vectors. They are:
- `dot(<vector>)` to get the dot product of two vectors.
- `cross(<vector>)` to get the cross product of two vectors. This is only available for 3D vectors.
- `distance(<vector>)` to get the distance between two vectors. This is equivalent to `(<current_vector> - <vector>).magnitude`. Note that in case of vectors with different dimensions, the distance will be calculated with the number of dimensions of the smallest vector.
- `normalize()` to normalize the vector. This modifies the original vector.

```python
vec_a = vec3(1, 2, 3)
vec_b = vec3(4, 5, 6)

print(vec_a.dot(vec_b)) # 32
print(vec_a.cross(vec_b)) # vec3(-3, 6, -3)

print(vec_a.distance(vec_b)) # 5.196152422706632
print(vec_a.normalize()) # vec3(0.2672612419124244, 0.5345224838248488, 0.8017837257372732)
```



## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [GLSL](https://www.khronos.org/opengl/wiki/Core_Language_(GLSL)) for the inspiration.

## Upcoming features

- [ ] Matrices
- [ ] Modifying multiple components at once (eg. `vec.xz = vec2(1, 2)`)