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

print(f"v1 + v2 = {v1 + v2}\n"
      f"v1 - v2 = {v1 - v2}\n"
      f"v1 * v2 = {v1 * v2}\n"
      f"v1 * 2 = {v1 * 2}\n"
      f"2 * v1 = {2 * v1}\n"
      f"v1.magnitude = {v1.magnitude}\n"
      f"v1.normalize() = {v1.normalize()}\n"
      f"v1.dot(v2) = {v1.dot(v2)}\n")

print(f"v1 == v2 = {v1 == v2}\n"
      f"v1 != v2 = {v1 != v2}\n"
      f"v1 == vec2(1, 2) = {v1 == vec2(1, 2)}\n")


print("\n> Testing vec3() operations")
v3 = vec3(1, 2, 3)
v4 = vec3(4, 5, 6)
print(f"v3 = {v3} and v2 = {v2}\n")

print(f"v3.size = {v3.size}\n")

print(f"v3.x = {v3.x}\n"
      f"v3.y = {v3.y}\n"
      f"v3.z = {v3.z}\n"
      f"v3.xy = {v3.xy}\n"
      f"v3.yz = {v3.yz}\n"
      f"v3.zx = {v3.zx}\n"
      f"v3.xyz = {v3.xyz}\n"
      f"v3.yxz = {v3.yxz}\n"
      f"v3.zxy = {v3.zxy}\n")

print(f"v3 + v4 = {v3 + v4}\n"
      f"v3 - v4 = {v3 - v4}\n"
      f"v3 * v4 = {v3 * v4}\n"
      f"v3 * 2 = {v3 * 2}\n"
      f"2 * v3 = {2 * v3}\n"
      f"v3.magnitude = {v3.magnitude}\n"
      f"v3.normal = {v3.normal}\n"
      f"v3 = {v3}\n"
      f"v3.normalize() = {v3.normalize()}\n"
      f"v3 = {v3}\n"
      f"v3.dot(v4) = {v3.dot(v4)}\n")

print(f"v3 == v4 = {v3 == v4}\n"
      f"v3 != v4 = {v3 != v4}\n"
      f"v3 == vec3(1, 2, 3) = {v3 == vec3(1, 2, 3)}\n")



