from glsyntax import *


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


print("\n> Testing vec4() operations")
v5 = vec4(1, 2, 3, 4)
v6 = vec4(5, 6, 7, 8)
print(f"v5 = {v5} and v6 = {v6}\n")

print(f"v5.size = {v5.size}\n")

print(f"v5.x = {v5.x}\n"
      f"v5.y = {v5.y}\n"
      f"v5.z = {v5.z}\n"
      f"v5.w = {v5.w}\n"
      f"v5.xy = {v5.xy}\n"
      f"v5.yz = {v5.yz}\n"
      f"v5.zw = {v5.zw}\n"
      f"v5.xyz = {v5.xyz}\n"
      f"v5.yzw = {v5.yzw}\n"
      f"v5.zwx = {v5.zwx}\n"
      f"v5.xyzw = {v5.xyzw}\n"
      f"v5.yzwx = {v5.yzwx}\n"
      f"v5.zwxy = {v5.zwxy}\n")

print(f"v5 + v6 = {v5 + v6}\n"
      f"v5 - v6 = {v5 - v6}\n"
      f"v5 * v6 = {v5 * v6}\n"
      f"v5 * 2 = {v5 * 2}\n"
      f"2 * v5 = {2 * v5}\n"
      f"v5.magnitude = {v5.magnitude}\n"
      f"v5.normal = {v5.normal}\n"
      f"v5 = {v5}\n"
      f"v5.normalize() = {v5.normalize()}\n"
      f"v5 = {v5}\n"
      f"v5.dot(v6) = {v5.dot(v6)}\n")

print(f"v5 == v6 = {v5 == v6}\n"
      f"v5 != v6 = {v5 != v6}\n"
      f"vec4(1, 2, 3, 4).normal = {vec4(1, 2, 3, 4).normal}\n"
      f"vec4(1, 2, 3, 4).normalize = {vec4(1, 2, 3, 4).normalize()}\n"
      f"vec4(1, 2, 3, 4).normal == vec4(1, 2, 3, 4).normalize() = {vec4(1, 2, 3, 4).normal == vec4(1, 2, 3, 4).normalize()}\n")


print("\n> Testing vec2() and vec3() operations")
print(f"v2 = {v2} and v4 = {v4}\n")


print(f"v2 + v4 = {v2 + v4}\n"
      f"v2 - v4 = {v2 - v4}\n"
      f"v2 * v4 = {v2 * v4}\n"
      f"v2 * 2 = {v2 * 2}\n"
      f"2 * v2 = {2 * v2}\n"
      f"v2.magnitude = {v2.magnitude}\n"
      f"v2.normalize() = {v2.normalize()}\n"
      f"v2.dot(v4) = {v2.dot(v4)}\n")

print(f"v2 == v4 = {v2 == v4}\n"
      f"v2 != v4 = {v2 != v4}\n"
      f"v2 == vec2(1, 2) = {v2 == vec2(1, 2)}\n")

print("\n> Testing advanced declarations")
v7 = vec3(1)

print(f"v7 = {v7}\n")

v8 = vec4(2, vec2(1.5), 0)

print(f"v8 = {v8}\n")
print(f"v8.wxw = {v8.wxw}\n")

v9 = vec4(v7.y, v8.xzw)

print(f"v9 = {v9}\n")

v9.x = 5
print(f"v9 = {v9}\n")

v9.yz = vec2(6, 7)

print(f"v9 = {v9}\n")
