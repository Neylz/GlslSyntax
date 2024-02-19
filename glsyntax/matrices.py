from .vectors import *
from typing import Tuple, Union

_Number = Union[int, float]
_Vector = Union[vec2, vec3, vec4]
_Matrix = Union['_mat2', '_mat3', '_mat4']

_ATTRIBUTES = "xyzw"
_ATTRIBUTES_ALIASES = "rgba"


class _matBase(object):
    _N = 0
    _M = 0

    def _get_name(self) -> str:
        if self.isSquare():
            return f"mat{self._N}"
        else:
            return f"mat{self._N}_{self._M}"

    def __init__(self, *args):
        if len(args) == 1:
            if isinstance(args[0], _Vector):
                if args[0].size != self._N:
                    raise ValueError(f"Invalid size for a vector: {args[0].size} (expected {self._N})")
                self.mat = [args[0] for _ in range(self._M)]
                return
            elif isinstance(args[0], _Number):
                # create a diagonal matrix with the same value
                self.mat = [empty_vec(self._N) for _ in range(self._M)]
                for i in range(min(self._N, self._M)):
                    self.mat[i][i] = args[0]
                return

        # count the number of arguments
        n_data = 0
        for arg in args:
            if isinstance(arg, _Number):
                n_data += 1
            elif isinstance(arg, _Vector):
                n_data += arg.size
            elif isinstance(arg, _Matrix):
                n_data += arg.size[0] * arg.size[1]
            else:
                raise ValueError(f"Invalid type for {self._get_name()}: {type(arg)}")

        if n_data != self._N * self._M:
            raise ValueError(
                f"Invalid number of arguments for {self._get_name()}: {n_data} (expected {self._N * self._M})")
        else:
            # set the attributes
            self.mat = [empty_vec(self._N, 0) for _ in range(self._M)]
            i = 0
            for arg in args:
                if isinstance(arg, _Number):
                    self.mat[i // self._N][i % self._N] = arg
                    i += 1
                elif isinstance(arg, _Vector):
                    for j in range(arg.size):
                        self.mat[i // self._N][i % self._N] = arg[j]
                        i += 1
                elif isinstance(arg, _Matrix):
                    for j in range(arg.size[0]):
                        for k in range(arg.size[1]):
                            self.mat[i // self._N][i % self._N] = arg[j][k]
                            i += 1

    def __repr__(self) -> str:
        return f"{self._get_name()}{self.mat}"

    def fprint(self) -> None:
        strout = f"{self._get_name()}["
        tab = " " * (len(strout))
        for i in range(self._M):
            if i != 0:
                strout += tab
            strout += f"{self.mat[i]}"
            if i != self._M-1:
                strout += "\n"
        strout += "]"
        print(strout)

    def __getitem__(self, key: int) -> _Vector:
        return self.mat[key]

    def __setitem__(self, key: int, value: _Vector) -> None:
        if value.size != self._N:
            raise ValueError(f"Invalid size for a vector: {value.size} (expected {self._N})")
        self.mat[key] = value

    def isSquare(self) -> bool:
        return self._N == self._M

    @property
    def size(self) -> Tuple[int, int]:
        return self._N, self._M


class mat2(_matBase):
    _N = 2
    _M = 2


class mat3(_matBase):
    _N = 3
    _M = 3


class mat4(_matBase):
    _N = 4
    _M = 4
