from typing import Any, Self, Union, Tuple

_Number = Union[int, float]

_ATTRIBUTES = "xyzw"
_ATTRIBUTES_ALIASES = "rgba"


class _vecBase(object):
    _N = 0

    def __getattr__(self, item):
        if (len(item) <= self._N) and (set(item).issubset(_ATTRIBUTES[:2]) or set(item).issubset(_ATTRIBUTES_ALIASES[:2])):
            if _ATTRIBUTES_ALIASES.find(item[0]) != -1:
                for char in item:
                    print(char)
                    item = item.replace(char, _ATTRIBUTES[_ATTRIBUTES_ALIASES.find(char)])
            match len(item):
                case 1:
                    return getattr(self, item[0])
                case 2:
                    return vec2(getattr(self, item[0]), getattr(self, item[1]))

        else:
            raise AttributeError(f"'vec2' object has no attribute '{item}'")

    @property
    def size(self) -> int:
        return self._N


class _matBase(_vecBase):
    _M = 0

    def __getattr__(self, item):
        pass

    @property
    def size(self) -> Tuple[int, int]:
        return self._N, self._M


class vec2(_vecBase):
    _N = 2

    def __init__(self, x: Union[_Number, Self], y: _Number = None):
        if y is None:
            if isinstance(x, vec2):
                self.x = x.x
                self.y = x.y
            else:
                raise ValueError(f"Invalid value for vec2: {x}")
        else:
            self.x = x
            self.y = y

    def __repr__(self) -> str:
        return f"vec2({self.x}, {self.y})"

    def __add__(self, b: Self) -> Self:
        return vec2(self.x + b.x, self.y + b.y)

    def __sub__(self, b: Self) -> Self:
        return vec2(self.x - b.x, self.y - b.y)

    def __mul__(self, b: Any) -> Self:
        if isinstance(b, (int, float)):
            return vec2(
                self.x * b,
                self.y * b
            )
        elif isinstance(b, vec2):
            return vec2(
                self.x * b.x,
                self.y * b.y
            )
        else:
            return NotImplemented

    def __rmul__(self, b: Any) -> Self:
        if isinstance(b, (int, float)):
            return vec2(
                self.x * b,
                self.y * b
            )
        else:
            return NotImplemented

    def length(self) -> Any:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def normalize(self) -> Self:
        self_length = self.length()
        return vec2(
            self.x / self_length,
            self.y / self_length
        )

    def dot(self, b: Self) -> Any:
        return self.x * b.x + self.y * b.y

# class vec3 (object):
#     def __init__(self, x: Any, y: Any, z: Any):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def __add__(self, b: Self) -> Self:
#         return vec3(self.x + b.x, self.y + b.y, self.z + b.z)
#
#     def __sub__(self, b: Self) -> Self:
#         return vec3(self.x - b.x, self.y - b.y, self.z - b.z)
#
#     def __mul__(self, b: Union[Self, int, float, 'mat3']) -> Self:
#         if isinstance(b, (int, float)):
#             return vec3(
#                 self.x * b,
#                 self.y * b,
#                 self.z * b
#             )
#         elif isinstance(b, mat3):
#             return vec3(
#                 self.x * b.m00 + self.y * b.m10 + self.z * b.m20,
#                 self.x * b.m01 + self.y * b.m11 + self.z * b.m21,
#                 self.x * b.m02 + self.y * b.m12 + self.z * b.m22
#             )
#         elif isinstance(b, vec3):
#             return vec3(
#                 self.x * b.x,
#                 self.y * b.y,
#                 self.z * b.z
#             )
#         else:
#             return NotImplemented
#
#
#
# class mat2 (object):
#     def __init__(self, a: Any, b: Any, c: Any, d: Any):
#         self.a = a
#         self.b = b
#         self.c = c
#         self.d = d
#
#     def __mul__(self, b: Self) -> Self:
#         return mat2(
#             self.a * b.a + self.b * b.c, self.a * b.b + self.b * b.d,
#             self.c * b.a + self.d * b.c, self.c * b.b + self.d * b.d
#         )
#
#     # def __mul__(self, b: vec2) -> vec2:
#     #     return vec2(self.a * b.x + self.b * b.y, self.c * b.x + self.d * b.y)
#
#
# class mat3 (object):
#     def __init__(self, m00: Any, m01: Any, m02: Any, m10: Any, m11: Any, m12: Any, m20: Any, m21: Any, m22: Any):
#         self.m00 = m00
#         self.m01 = m01
#         self.m02 = m02
#         self.m10 = m10
#         self.m11 = m11
#         self.m12 = m12
#         self.m20 = m20
#         self.m21 = m21
#         self.m22 = m22
#
#     def __add__(self, b: Self) -> Self:
#         return mat3(
#             self.m00 + b.m00, self.m01 + b.m01, self.m02 + b.m02,
#             self.m10 + b.m10, self.m11 + b.m11, self.m12 + b.m12,
#             self.m20 + b.m20, self.m21 + b.m21, self.m22 + b.m22
#         )
#
#     def __sub__(self, b: Self) -> Self:
#         return mat3(
#             self.m00 - b.m00, self.m01 - b.m01, self.m02 - b.m02,
#             self.m10 - b.m10, self.m11 - b.m11, self.m12 - b.m12,
#             self.m20 - b.m20, self.m21 - b.m21, self.m22 - b.m22
#         )
#
#     def __mul__(self, b: Any) -> Union[Self, vec3]:
#         if isinstance(b, mat3):
#             return mat3(
#                 self.m00 * b.m00 + self.m01 * b.m10 + self.m02 * b.m20,
#                 self.m00 * b.m01 + self.m01 * b.m11 + self.m02 * b.m21,
#                 self.m00 * b.m02 + self.m01 * b.m12 + self.m02 * b.m22,
#
#                 self.m10 * b.m00 + self.m11 * b.m10 + self.m12 * b.m20,
#                 self.m10 * b.m01 + self.m11 * b.m11 + self.m12 * b.m21,
#                 self.m10 * b.m02 + self.m11 * b.m12 + self.m12 * b.m22,
#
#                 self.m20 * b.m00 + self.m21 * b.m10 + self.m22 * b.m20,
#                 self.m20 * b.m01 + self.m21 * b.m11 + self.m22 * b.m21,
#                 self.m20 * b.m02 + self.m21 * b.m12 + self.m22 * b.m22
#             )
#         elif isinstance(b, vec3):
#             return vec3(
#                 self.m00 * b.x + self.m01 * b.y + self.m02 * b.z,
#                 self.m10 * b.x + self.m11 * b.y + self.m12 * b.z,
#                 self.m20 * b.x + self.m21 * b.y + self.m22 * b.z
#             )
#         else:
#             return NotImplemented
