from typing import Any, Self, Union, Tuple

_Number = Union[int, float]

_ATTRIBUTES = "xyzw"
_ATTRIBUTES_ALIASES = "rgba"


class _vecBase(object):
    _N = 0

    def __init__(self, *args: Union[_Number, Self]):
        # count the number of arguments
        n_data = 0
        for arg in args:
            if isinstance(arg, _Number):
                n_data += 1
            elif isinstance(arg, _vecBase):
                n_data += arg.size
            else:
                raise ValueError(f"Invalid type for vec{self._N}: {type(arg)}")

        if n_data != self._N:
            raise ValueError(f"Invalid number of arguments for vec{self._N}: {n_data} (expected {self._N})")
        else:
            # set the attributes
            i = 0
            for arg in args:
                if isinstance(arg, _Number):
                    setattr(self, _ATTRIBUTES[i], arg)
                    i += 1
                elif isinstance(arg, _vecBase):
                    for j in range(arg.size):
                        setattr(self, _ATTRIBUTES[i], getattr(arg, _ATTRIBUTES[j]))
                        i += 1


    def __repr__(self) -> str:
        return f"vec{self._N}({', '.join([str(getattr(self, attr)) for attr in _ATTRIBUTES[:self._N]])})"


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

    def __add__(self, b: Self) -> Self:
        return vec2(self.x + b.x, self.y + b.y)

    def __sub__(self, b: Self) -> Self:
        return vec2(self.x - b.x, self.y - b.y)

    def __mul__(self, b: Any) -> Self:
        if isinstance(b, _Number):
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
        if isinstance(b, _Number):
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



# class vec3 (_vecBase):
#     _N = 3
#
#     def __init__(self, x: Union[_Number, vec2, Self], y: Union[_Number, vec2] = None, z: _Number = None):
#         # vec3
#         if isinstance(x, vec3):
#             if y is not None:
#                 raise ValueError(f"Too many arguments for vec3: {x}, {y}")
#             if z is not None:
#                 raise ValueError(f"Too many arguments for vec3: {x}, {z}")
#             self.x = x.x
#             self.y = x.y
#             self.z = x.z
#         # vec2 + number
#         elif isinstance(x, vec2) and isinstance(y, _Number):
#             self.x = x.x
#             self.y = x.y
#             self.z = y
#         else:
#             raise ValueError(f"Invalid value for vec3: {x}")
#         # else:
#         #     if isinstance(x, _Number) and isinstance(y, _Number) and isinstance(z, _Number):
#         #         self.x = x
#         #         self.y = y
#         #         self.z = z
#         #     else:
#         #         raise ValueError(f"Invalid types for vec3: {x}:{type(x)}, {y}:{type(y)} and {z}:{type(z)}")
#
#     def __repr__(self) -> str:
#         return f"vec3({self.x}, {self.y}, {self.z})"
#
#     def __add__(self, b: Self) -> Self:
#         return vec3(self.x + b.x, self.y + b.y, self.z + b.z)
#
#     def __sub__(self, b: Self) -> Self:
#         return vec3(self.x - b.x, self.y - b.y, self.z - b.z)
#
#     def __mul__(self, b: Any) -> Self:
#         if isinstance(b, _Number):
#             return vec3(
#                 self.x * b,
#                 self.y * b,
#                 self.z * b
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
#     def __rmul__(self, b: Any) -> Self:
#         if isinstance(b, _Number):
#             return vec3(
#                 self.x * b,
#                 self.y * b,
#                 self.z * b
#             )
#         else:
#             return NotImplemented
#
#     def length(self) -> Any:
#         return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5
#
#     def normalize(self) -> Self:
#         self_length = self.length()
#         return vec3(
#             self.x / self_length,
#             self.y / self_length,
#             self.z / self_length
#         )
#
#     def dot(self, b: Self) -> Any:
#         return self.x * b.x + self.y * b.y + self.z * b.z
#
#
#
#
