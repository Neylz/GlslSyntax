from typing import Self, Union, Any

_Number = Union[int, float]
_Vector = Union["vec2", "vec3", "vec4"]

_ATTRIBUTES = "xyzw"
_ATTRIBUTES_ALIASES = "rgba"


def array_to_vec(array: list[_Number]) -> Union[_Number, _Vector]:
    match len(array):
        case 1:
            return array[0]
        case 2:
            return vec2(*array)
        case 3:
            return vec3(*array)
        case 4:
            return vec4(*array)
        case _:
            raise ValueError(f"Invalid number of elements for a vector: {len(array)} (expected <= 4)")



class _vecBase(object):
    _N = 0

    def __init__(self, *args: Union[_Number, Self]):
        if len(args) == 1 and isinstance(args[0], _Number):
            for i in range(self._N):
                setattr(self, _ATTRIBUTES[i], args[0])
            return
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

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, _vecBase):
            return False
        return all([getattr(self, attr) == getattr(other, attr) for attr in _ATTRIBUTES[:self._N]])

    def __ne__(self, other: Any) -> bool:
        if not isinstance(other, _vecBase):
            return True
        return not self == other

    def __mul__(self, other: Union[_Number, _Vector]) -> Union[Self, _Number]:
        # vector * scalar
        if isinstance(other, _Number):
            return type(self)(*[getattr(self, attr) * other for attr in _ATTRIBUTES[:self._N]])
        # vector * vector (component-wise)
        elif isinstance(other, _vecBase):
            # select the minimum size
            size = min(self._N, other._N)
            if self._N <= other._N:
                return type(self)(*[getattr(self, attr) * getattr(other, attr) for attr in _ATTRIBUTES[:size]])
            else:
                return type(other)(*[getattr(self, attr) * getattr(other, attr) for attr in _ATTRIBUTES[:size]])

        else:
            return NotImplemented

    def __rmul__(self, other: _Number) -> Self:
        # scalar * vector
        return type(self)(*[other * getattr(self, attr) for attr in _ATTRIBUTES[:self._N]])

    def __add__(self, other: Union[_Number, _Vector]) -> Self:
        if isinstance(other, _Number):
            return type(self)(*[getattr(self, attr) + other for attr in _ATTRIBUTES[:self._N]])
        elif isinstance(other, _vecBase):
            size = min(self._N, other._N)
            if self._N <= other._N:
                return type(self)(*[getattr(self, attr) + getattr(other, attr) for attr in _ATTRIBUTES[:size]])
            else:
                return type(other)(*[getattr(self, attr) + getattr(other, attr) for attr in _ATTRIBUTES[:size]])

        else:
            return NotImplemented

    def __radd__(self, other: _Number) -> Self:
        # add the scalar to each component
        return type(self)(*[getattr(self, attr) + other for attr in _ATTRIBUTES[:self._N]])

    def __sub__(self, other: Union[_Number, _Vector]) -> Self:
        if isinstance(other, _Number):
            return type(self)(*[getattr(self, attr) - other for attr in _ATTRIBUTES[:self._N]])
        elif isinstance(other, _vecBase):
            size = min(self._N, other._N)
            if self._N <= other._N:
                return type(self)(*[getattr(self, attr) - getattr(other, attr) for attr in _ATTRIBUTES[:size]])
            else:
                return type(other)(*[getattr(self, attr) - getattr(other, attr) for attr in _ATTRIBUTES[:size]])
        else:
            return NotImplemented

    def __rsub__(self, other: _Number) -> Self:
        return type(self)(*[other - getattr(self, attr) for attr in _ATTRIBUTES[:self._N]])

    def __truediv__(self, other: Union[_Number, _Vector]) -> Self:
        if isinstance(other, _Number):
            # divide each component by the scalar
            return type(self)(*[getattr(self, attr) / other for attr in _ATTRIBUTES[:self._N]])
        elif isinstance(other, _vecBase):
            size = min(self._N, other._N)
            if self._N <= other._N:
                return type(self)(*[getattr(self, attr) / getattr(other, attr) for attr in _ATTRIBUTES[:size]])
            else:
                return type(other)(*[getattr(self, attr) / getattr(other, attr) for attr in _ATTRIBUTES[:size]])
        else:
            return NotImplemented

    def __rtruediv__(self, other: _Number) -> Self:
        # divide each component by the inverse of the scalar
        return type(self)(*[other / getattr(self, attr) for attr in _ATTRIBUTES[:self._N]])

    def __neg__(self) -> Self:
        return type(self)(*[-getattr(self, attr) for attr in _ATTRIBUTES[:self._N]])


    def __getattr__(self, item):
        if (len(item) <= self._N) and (
                set(item).issubset(_ATTRIBUTES[:self._N]) or set(item).issubset(_ATTRIBUTES_ALIASES[:self._N])):
            if _ATTRIBUTES_ALIASES.find(item[0]) != -1:
                for char in item:
                    print(char)
                    item = item.replace(char, _ATTRIBUTES[_ATTRIBUTES_ALIASES.find(char)])
            # return a new vector of the right size with the selected components
            return array_to_vec([getattr(self, attr) for attr in item])

        else:
            raise AttributeError(f"'vec{self._N}' object has no attribute '{item}'")

    @property
    def size(self) -> int:
        return self._N

    @property
    def magnitude(self) -> _Number:
        return sum([getattr(self, attr) ** 2 for attr in _ATTRIBUTES[:self._N]]) ** 0.5

    @property
    def normal(self) -> Self:
        # return a new vector without modifying the original
        m = self.magnitude
        return type(self)(*[getattr(self, attr) / m for attr in _ATTRIBUTES[:self._N]])


    def dot(self, other: _Vector) -> _Number:
        # dot product
        size = min(self.size, other.size)
        return sum([getattr(self, attr) * getattr(other, attr) for attr in _ATTRIBUTES[:size]])

    def normalize(self) -> Self:
        # modify the vector in place
        m = self.magnitude
        for attr in _ATTRIBUTES[:self._N]:
            setattr(self, attr, getattr(self, attr) / m)
        return self






class vec2(_vecBase):
    _N = 2


class vec3(_vecBase):
    _N = 3


class vec4(_vecBase):
    _N = 4

