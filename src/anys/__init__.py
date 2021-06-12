"""
Matchers for pytest

Visit <https://github.com/jwodder/anys> for more information.
"""

__version__ = "0.1.0.dev1"
__author__ = "John Thorvald Wodder II"
__author_email__ = "anys@varonathe.org"
__license__ = "MIT"
__url__ = "https://github.com/jwodder/anys"

import sys
import types
from typing import Any, Callable, Generic, Optional, Tuple, TypeVar, Union

T = TypeVar("T")

if sys.version_info[:2] >= (3, 10):
    InstanceCls = Union[
        type, types.Union, Tuple[Union[type, types.Union, Tuple[Any, ...]], ...]
    ]
else:
    InstanceCls = Union[type, Tuple[Union[type, Tuple[Any, ...]], ...]]


class AnyRepr(Generic[T]):
    def __init__(self, arg: T) -> None:
        self.arg = arg

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.arg!r})"


class AnyFunc(AnyRepr[Callable]):
    def __eq__(self, other: Any) -> bool:
        return bool(self.arg(other))


class AnyInstance:
    def __init__(self, arg: InstanceCls, *, name: Optional[str] = None) -> None:
        self.arg = arg
        self.name = name

    def __repr__(self) -> str:
        if self.name is not None:
            return self.name
        else:
            return f"{type(self).__name__}({self.arg!r})"

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, self.arg)


ANY_STR = AnyInstance(str, name="ANY_STR")
ANY_INT = AnyInstance(int, name="ANY_INT")
