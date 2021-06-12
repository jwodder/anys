"""
Matchers for pytest

Visit <https://github.com/jwodder/anys> for more information.
"""

__version__ = "0.1.0.dev1"
__author__ = "John Thorvald Wodder II"
__author_email__ = "anys@varonathe.org"
__license__ = "MIT"
__url__ = "https://github.com/jwodder/anys"

from abc import ABC, abstractmethod
import sys
import types
from typing import Any, Callable, Generic, Optional, Tuple, TypeVar, Union

T = TypeVar("T")

if sys.version_info[:2] >= (3, 10):
    ClassInfo = Union[
        type, types.Union, Tuple[Union[type, types.Union, Tuple[Any, ...]], ...]
    ]
else:
    ClassInfo = Union[type, Tuple[Union[type, Tuple[Any, ...]], ...]]


class AnyBase(ABC):
    @abstractmethod
    def match(self, value: Any) -> bool:
        ...

    def __eq__(self, other: Any) -> bool:
        try:
            return self.match(other)
        except (TypeError, ValueError):
            return False


class AnyRepr(Generic[T]):
    def __init__(self, arg: T) -> None:
        self.arg = arg

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.arg!r})"


class AnyFunc(AnyRepr[Callable], AnyBase):
    def match(self, value: Any) -> bool:
        return bool(self.arg(value))


class AnyInstance(AnyBase):
    def __init__(self, arg: ClassInfo, *, name: Optional[str] = None) -> None:
        self.arg = arg
        self.name = name

    def __repr__(self) -> str:
        if self.name is not None:
            return self.name
        else:
            return f"{type(self).__name__}({self.arg!r})"

    def match(self, value: Any) -> bool:
        return isinstance(value, self.arg)


# Anys need to be constructed via functions that return typing.Any so that
# comparing them doesn't trigger a "comparison-overlap" type error.


def any_func(func: Callable) -> Any:
    return AnyFunc(func)


def any_instance(classinfo: ClassInfo, *, name: Optional[str] = None) -> Any:
    return AnyInstance(classinfo, name=name)


ANY_STR = any_instance(str, name="ANY_STR")
ANY_INT = any_instance(int, name="ANY_INT")
