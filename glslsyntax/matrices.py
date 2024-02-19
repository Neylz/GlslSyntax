from .vectors import *
from typing import Tuple, Union, List

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

    def __init__(self, *args: Union[_Number, _Vector, _Matrix, List[_Number], List[List[_Number]]]):
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
            elif isinstance(arg, _matBase):
                n_data += arg.size[0] * arg.size[1]
            elif isinstance(arg, list) and all(isinstance(e, _Number) for e in arg):
                n_data += len(arg)
            elif isinstance(arg, list) and all(isinstance(e, list) for e in arg):
                n_data += sum(len(e) for e in arg)
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
                elif isinstance(arg, _matBase):
                    for j in range(arg.size[0]):
                        for k in range(arg.size[1]):
                            self.mat[i // self._N][i % self._N] = arg[j][k]
                            i += 1
                elif isinstance(arg, list) and all(isinstance(e, _Number) for e in arg):
                    for j in arg:
                        self.mat[i // self._N][i % self._N] = j
                        i += 1
                elif isinstance(arg, list) and all(isinstance(e, list) for e in arg):
                    for e in arg:
                        for j in e:
                            self.mat[i // self._N][i % self._N] = j
                            i += 1

    def __add__(self, other: Union[_Matrix, _Number]) -> Self:
        if isinstance(other, _matBase):
            if self.size != other.size:
                raise ValueError(f"Invalid size for a matrix: {other.size} (expected {self.size})")
            return self.__class__(*[self[i] + other[i] for i in range(self._M)])
        elif isinstance(other, _Number):
            return self.__class__(*[self[i] + other for i in range(self._M)])

    def __radd__(self, other: _Number) -> Self:
        return self.__class__(*[self[i] + other for i in range(self._M)])

    def __sub__(self, other: Union[_Matrix, _Number]) -> Self:
        if isinstance(other, _matBase):
            if self.size != other.size:
                raise ValueError(f"Invalid size for a matrix: {other.size} (expected {self.size})")
            return self.__class__(*[self[i] - other[i] for i in range(self._M)])
        elif isinstance(other, _Number):
            return self.__class__(*[self[i] - other for i in range(self._M)])

    def __rsub__(self, other: _Number) -> Self:
        return self.__class__(*[other - self[i] for i in range(self._M)])

    def __mul__(self, other: Union[_Matrix, _Number]) -> Self:
        if isinstance(other, _matBase):
            if self._N != other.size[1]:
                raise ValueError(f"Invalid size for a matrix: {other.size} (expected {self.size})")
            else:
                res = [[0 for _ in range(other.size[1])] for _ in range(self._N)]
                for i in range(self._N):
                    for j in range(other.size[1]):
                        for k in range(self._M):
                            res[i][j] += self[i][k] * other[k][j]
                return self.__class__(*res)

        elif isinstance(other, _Number):
            return self.__class__(*[self[i] * other for i in range(self._M)])

    def __rmul__(self, other: _Number) -> Self:
        return self.__class__(*[self[i] * other for i in range(self._M)])

    def __truediv__(self, other: Union[_Number, _Matrix]) -> Self:
        if isinstance(other, _matBase):
            # make it component-wise
            if self.size != other.size:
                raise ValueError(f"Invalid size for a matrix: {other.size} (expected {self.size})")
            else:
                return self.__class__(*[self[i] / other[i] for i in range(self._M)])
        else:
            return self.__class__(*[self[i] / other for i in range(self._M)])

    def __rtruediv__(self, other: _Number) -> Self:
        return self.__class__(*[other / self[i] for i in range(self._M)])

    def __neg__(self) -> Self:
        return self.__class__(*[-self[i] for i in range(self._M)])

    def __eq__(self, other: _Matrix) -> bool:
        if not isinstance(other, _matBase):
            return False
        if self.size != other.size:
            return False
        for i in range(self._M):
            if self[i] != other[i]:
                return False
        return True

    def __ne__(self, other: _Matrix) -> bool:
        return not self.__eq__(other)   

    def __getitem__(self, key: int) -> _Vector:
        return self.mat[key]

    def __setitem__(self, key: int, value: _Vector) -> None:
        if value.size != self._N:
            raise ValueError(f"Invalid size for a vector: {value.size} (expected {self._N})")
        self.mat[key] = value

    def __repr__(self) -> str:
        return f"{self._get_name()}{self.mat}"

    def fprint(self) -> None:
        strout = f"{self._get_name()}["
        tab = " " * (len(strout))
        for i in range(self._M):
            if i != 0:
                strout += tab
            strout += f"{self.mat[i]}"
            if i != self._M - 1:
                strout += "\n"
        strout += "]"
        print(strout)

    def isSquare(self) -> bool:
        return self._N == self._M

    def isDiagonal(self) -> bool:
        for i in range(self._M):
            for j in range(self._N):
                if i != j and self[i][j] != 0:
                    return False
        return True

    def isSymmetric(self) -> bool:
        if not self.isSquare():
            return False
        for i in range(self._M):
            for j in range(i):
                if self[i][j] != self[j][i]:
                    return False
        return True

    def isIdentity(self) -> bool:
        if not self.isSquare():
            return False
        for i in range(self._M):
            for j in range(self._N):
                if i == j and self[i][j] != 1:
                    return False
                elif i != j and self[i][j] != 0:
                    return False
        return True

    def isOrthogonal(self) -> bool:
        if not self.isSquare():
            return False
        return self * self.T == self.Id


    def getArray(self) -> List[List[_Number]]:
        return [self[i].getArray() for i in range(self._M)]


    def __det(self, mat: List[List[_Number]]) -> _Number:
        if len(mat) == 1:
            return mat[0][0]
        else:
            res = 0
            for i in range(len(mat)):
                submat = [mat[j][:i] + mat[j][i + 1:] for j in range(1, len(mat))]
                res += ((-1) ** i) * mat[0][i] * self.__det(submat)
            return res

    @property
    def det(self) -> _Number:
        if not self.isSquare():
            raise ValueError("Determinant is only defined for square matrices")
        else:
            return self.__det(self.getArray())

    def transpose(self) -> Self:
        # modify the matrix in place by transposing it
        self.mat = self.T.mat
        return self

    @property
    def T(self) -> Self:
        # return a new transposed matrix
        res = [empty_vec(self._M) for _ in range(self._N)]
        for i in range(self._M):
            for j in range(self._N):
                res[j][i] = self[i][j]
        return self.__class__(*res)

    @property
    def Id(self) -> Self:
        if self.isSquare():
            # return a new identity matrix
            res = [empty_vec(self._N) for _ in range(self._M)]
            for i in range(self._M):
                res[i][i] = 1
            return self.__class__(*res)
        else:
            raise ValueError("Identity matrix must be square")


    def __inverse(self, mat: List[List[_Number]]) -> List[List[_Number]]:
        det = self.__det(mat)
        if det == 0:
            raise ValueError("Matrix is not invertible")
        else:
            inverse_matrix = [[0 for _ in range(self._N)] for _ in range(self._M)]
            for i in range(self._M):
                for j in range(self._N):
                    submat = [row[:j] + row[j + 1:] for k, row in enumerate(mat) if k != i]
                    inverse_matrix[i][j] = ((-1) ** (i + j)) * self.__det(submat) / det
            return inverse_matrix
            

    @property
    def Inv(self):
        if not self.isSquare():
            raise ValueError("Inverse is only defined for square matrices")
        else:
            return self.__class__(*self.__inverse(self.getArray())).transpose()

    def invert(self) -> Self:
        self.mat = self.Inv.mat
        return self

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


class mat2x3(_matBase):
    _N = 2
    _M = 3


class mat3x2(_matBase):
    _N = 3
    _M = 2


class mat2x4(_matBase):
    _N = 2
    _M = 4


class mat4x2(_matBase):
    _N = 4
    _M = 2


class mat3x4(_matBase):
    _N = 3
    _M = 4


class mat4x3(_matBase):
    _N = 4
    _M = 3
