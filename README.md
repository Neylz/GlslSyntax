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
u = vec2(1, 2.3)
v = vec3(1, 2, 3)
w = vec4(1, 2, 3, 4)

# Shorthand declaration
u2 = vec2(1) # (1, 1)
v2 = vec3(1.1) # (1.1, 1.1, 1.1)
w2 = vec4(1) # (1, 1, 1, 1)
```

You can also use other vectors to create a new one.
```python
u3 = vec4(vec2(1), vec2(3, 4)) # (1, 1, 3, 4)
v3 = vec3(1, vec2(2, 3.5)) # (1, 2, 3.5)
```

#### Attributes

All vectors have the following attributes:
- `x`, `y`, `z`, `w` to access the components of the vector. `x` and `y` are always available, `z` is available for 3D and 4D vectors, and `w` is available for 4D vectors.
- `r`, `g`, `b`, `a` are aliases for `x`, `y`, `z`, `w` and acts in the same way.
- `magnitude` to get the magnitude of the vector.
- `normal` to get the normalized vector. This doesn't modify the original vector.
- `size` to get the number of dimensions of the vector.

##### Swizzling

The `x`, `y`, `z`, `w` attributes can be used together to create a new vector with a number of dimensions equal to the number of attributes used. The order of the attributes will affect the order of the components in the new vector.
```python
u = vec3(1, 2, 3)

v = u.yzx # vec3(2, 3, 1)
w = u.zzz # vec3(3, 3, 3)

print(u.magnitude) # 3.7416573867739413
print(u.normal.x) # 0.2672612419124244
print(u.xz.size) # 2
```


The `x`, `y`, `z`, `w` attributes can be used to set the components of the vector.

```python
u = vec3(1, 2, 3)
u.x = 4

print(vec) # vec3(4, 2, 3)
```

#### Access values by index
For iteratives approaches, you can access the components of the vector by index.
Though, this can return only a single value, not a vector.

```python
u = vec3(1, 2, 3)

# Accessing by index
print(u[0]) # 1
print(u[1]) # 2
print(u[2]) # 3

# Modifying by index
u[0] = 4
print(u) # vec3(4, 2, 3)
```
This functionality exists for better matrix manipulations.


#### Methods

Some functions of GLSL have been implemented as methods of the vectors. They are:
- `dot(<vector>)` to get the dot product of two vectors.
- `cross(<vector>)` to get the cross product of two vectors. This is only available for 3D vectors.
- `distance(<vector>)` to get the distance between two vectors. This is equivalent to `(<current_vector> - <vector>).magnitude`. Note that in case of vectors with different dimensions, the distance will be calculated with the number of dimensions of the smallest vector.
- `normalize()` to normalize the vector. This modifies the original vector contrary to the `normal` attribute. Returns the normalized vector.
- `getArray()` to get the components of the vector as a list.

```python
u = vec3(1, 2, 3)
v = vec3(4, 5, 6)

print(u.dot(v)) # 32
print(u.cross(v)) # vec3(-3, 6, -3)

print(u.distance(v)) # 5.196152422706632
print(u.normalize()) # vec3(0.2672612419124244, 0.5345224838248488, 0.8017837257372732)
```

#### Operators

The following operators are available for vectors:
- `+` to add two vectors.
- `-` to subtract two vectors.
- `*` to multiply a vector by a scalar or to get the component-wise product of two vectors.
- `/` to divide a vector by a scalar or to get the component-wise division of two vectors.

> [!IMPORTANT]
> When using two vectors with different dimensions, the operation will be done with the number of dimensions of the smallest vector.

```python
u = vec3(1, 2, 3)
v = vec3(4, 5, 6)

print(u + v) # vec3(5, 7, 9)
print(u - v) # vec3(-3, -3, -3)
print(u * 2) # vec3(2, 4, 6)
print(u / 2) # vec3(0.5, 1, 1.5)
print(u * v) # vec3(4, 10, 18)
print(u / v) # vec3(0.25, 0.4, 0.5)
```


### Matrices

#### Declaration

Matrices can be declared by typing `mat` followed by the number of rows and columns. Up to 4x4 matrices are supported. To declare the matrix.
> [!INFO]
> The arguments format follows the [GLSL matrix declaration](https://registry.khronos.org/OpenGL/specs/es/3.0/GLSL_ES_Specification_3.00.pdf#page=70). That means that the first argument is the first **column**, the second argument is the second **column**, and so on.

Here are some examples of matrix declaration:
```python
# Diagonal matrix
m = mat2(1) 
n = mat3(2)

# m is an identity matrix: 
# | 1 0 |
# | 0 1 |

# n is a diagonal matrix:
# | 2 0 0 |
# | 0 2 0 |
# | 0 0 2 |

o = mat2(1, 2,  # first column
         3, 4)  # second column
# o is a 2x2 matrix:
# | 1 3 |
# | 2 4 |
# but stored as:
# vec2(1, 2),
# vec2(3, 4)

p = mat3(vec3(1, 2, 3),  # first column
         vec3(4, 5, 6),  # second column
         vec3(7, 8, 9))  # third column
# p is a 3x3 matrix:
# | 1 4 7 |
# | 2 5 8 |
# | 3 6 9 |
# but stored as:
# vec3(1, 2, 3),
# vec3(4, 5, 6),
# vec3(7, 8, 9)
```

Additionally to the classic GLSL declaration, an extra feature of this package is the ability to input as arguments different types of vectors and matrices. If the arguments arn't vectors or matrices of the expected size but there are the right number of components, the package will try to create the matrix with the components of the arguments.

```python
u = vec2(1, 2)
v = vec2(3, 4)
w = vec3(5, 6, 7)

m = mat4(u, v, w, vec4(8, 9, 10, 11), vec4(12, 13, 14, 15), 16)
# m is a 4x4 matrix:
# | 1 5 9  13 |
# | 2 6 10 14 |
# | 3 7 11 15 |
# | 4 8 12 16 |
```

#### Attributes

All matrices have the following attributes:
- `size` returns a tuple with the number of columns (number of vectors) and raws of the matrix (size of the vectors).
- `T` returns the transpose of the matrix. This doesn't modify the original matrix.
- `Id` returns the identity matrix of the same size as the original matrix.
- `Inv` returns the inverse of the matrix. This doesn't modify the original matrix.
- `det` returns the determinant of the matrix.

#### Methods
- `getArray()` to get the components of the matrix as a list.
- `isSquare()` to check if the matrix is a square matrix.
- `isIdentity()` to check if the matrix is an identity matrix.
- `isDiagonal()` to check if the matrix is a diagonal matrix.
- `isSymmetric()` to check if the matrix is a symmetric matrix.
- `isOrthogonal()` to check if the matrix is an orthogonal matrix.
- `fprint()` to print the matrix in a formatted way.

#### Operators

The following operators are available for matrices:
- `+` to add two matrices of the same size or to add a scalar to each component of the matrix.
- `-` to subtract two matrices of the same size or to subtract a scalar to each component of the matrix.
- `*` to multiply a matrix by a scalar or to get the matrix product of two matrices.
- `/` to divide a matrix by a scalar or to divide a matrix by another matrix component-wise. The two matrices must have the same size.

#### Access values by index

For iteratives approaches, you can access the components of the matrix by index.

```python
m = mat2(1, 2,
         3, 4)

# Accessing by index
print(m[0][0]) # 1

# Modifying by index
m[0][0] = 5

print(m) # mat2(5, 2, 3, 4)

print(m[0]) # vec2(5, 3)

m[0] = vec2(1, 2)

print(m) # mat2(1, 2, 3, 4)
```


#### Examples

```python
m = mat2(1, 2,
         3, 4)

n = mat2(5, 6,
         7, 8)

print(m + n) # mat2(6, 8, 10, 12)
print(m - n) # mat2(-4, -4, -4, -4)
print(m * 2) # mat2(2, 4, 6, 8)
print(m / 2) # mat2(0.5, 1, 1.5, 2)
print(m * n) # mat2(19, 22, 43, 50)

print(m.T) # mat2(1, 3, 2, 4)
print(m.Id) # mat2(1, 0, 0, 1)
print(m.Inv) # mat2(-2, 1, 1.5, -0.5)
print(m.det) # -2
```



## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [GLSL](https://www.khronos.org/opengl/wiki/Core_Language_(GLSL)) for the inspiration.

## Upcoming features

- [x] Matrices
- [ ] Multiply matrices by vectors and other matrices of different sizes
- [ ] Modifying multiple components at once (eg. `vec.xz = vec2(1, 2)`)
- [x] Supoort lists as declaration arguments