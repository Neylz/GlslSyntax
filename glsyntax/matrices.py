from .vectors import _vecBase, _Number, _ATTRIBUTES
from typing import Tuple, Union


class _matBase(_vecBase):
    _M = 0

    def __getattr__(self, item):
        pass

    @property
    def size(self) -> Tuple[int, int]:
        return self._N, self._M

    

