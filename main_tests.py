from typing import Union
from glslvm import *


print("Testing the main functions of the GLSL Vectors and Matrices library")

print("\n> Testing vec2() operations")
v1 = vec2(1, 2)
v2 = vec2(3, 4)
print(f"v1 = {v1} and v2 = {v2}\n")

print(f"v1.size = {v1.size}\n")

print(f"v1.x = {v1.x}\n"
      f"v1.y = {v1.y}\n"
      f"v1.xy = {v1.xy}\n"
      f"v1.yx = {v1.yx}\n")

print("v1 + v2 =", v1 + v2)
print("v1 - v2 =", v1 - v2)
print("v1 * v2 =", v1 * v2)
print("v1 * 2 =", v1 * 2)
print("2 * v1 =", 2 * v1)
print("v1.length() =", v1.length())
print("v1.normalize() =", v1.normalize())
print("v1.dot(v2) =", v1.dot(v2))

print(f"v1 == v2 = {v1 == v2}\n"
      f"v1 != v2 = {v1 != v2}\n"
      f"v1 == vec2(1, 2) = {v1 == vec2(1, 2)}\n")

