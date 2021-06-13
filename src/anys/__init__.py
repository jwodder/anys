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
from collections.abc import Iterable, Iterator, Mapping, Sequence
from datetime import datetime
from numbers import Number
import re
import sys
import types
from typing import Any, AnyStr, Callable, Generic, List, Optional, Tuple, TypeVar, Union

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


class AnyRepr(AnyBase, Generic[T]):
    def __init__(self, arg: T) -> None:
        self.arg = arg

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.arg!r})"


class AnyFunc(AnyRepr[Callable]):
    def match(self, value: Any) -> bool:
        return bool(self.arg(value))


def any_func(func: Callable) -> Any:
    return AnyFunc(func)


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


def any_instance(classinfo: ClassInfo, *, name: Optional[str] = None) -> Any:
    return AnyInstance(classinfo, name=name)


ANY_BOOL = any_instance(bool, name="ANY_BOOL")
ANY_BYTES = any_instance(bytes, name="ANY_BYTES")
ANY_COMPLEX = any_instance(complex, name="ANY_COMPLEX")
ANY_DATETIME = any_instance(datetime, name="ANY_DATETIME")
ANY_DICT = any_instance(dict, name="ANY_DICT")
ANY_FLOAT = any_instance(float, name="ANY_FLOAT")
ANY_INT = any_instance(int, name="ANY_INT")
ANY_ITERABLE = any_instance(Iterable, name="ANY_ITERABLE")
ANY_ITERATOR = any_instance(Iterator, name="ANY_ITERATOR")
ANY_LIST = any_instance(list, name="ANY_LIST")
ANY_MAPPING = any_instance(Mapping, name="ANY_MAPPING")
ANY_NUMBER = any_instance(Number, name="ANY_NUMBER")
ANY_SEQUENCE = any_instance(Sequence, name="ANY_SEQUENCE")
ANY_SET = any_instance(set, name="ANY_SET")
ANY_STR = any_instance(str, name="ANY_STR")
ANY_TUPLE = any_instance(tuple, name="ANY_TUPLE")


class AnyAwareDatetime(AnyBase):
    def match(self, value: Any) -> bool:
        return isinstance(value, datetime) and value.tzinfo is not None

    def __repr__(self) -> str:
        return "ANY_AWARE_DATETIME"


ANY_AWARE_DATETIME: Any = AnyAwareDatetime()


class Maybe(AnyRepr[Any]):
    def match(self, value: Any) -> bool:
        return bool(value is None or self.arg == value)


def maybe(value: Any) -> Any:
    return Maybe(value)


class Not(AnyRepr[Any]):
    def match(self, value: Any) -> bool:
        return bool(self.arg != value)


def not_(value: Any) -> Any:
    return Not(value)


class AnyMatch(AnyRepr[Union[AnyStr, re.Pattern[AnyStr]]]):
    def match(self, value: Any) -> bool:
        return bool(re.match(self.arg, value))


def any_match(value: Union[AnyStr, re.Pattern[AnyStr]]) -> Any:
    return AnyMatch(value)


class AnySearch(AnyRepr[Union[AnyStr, re.Pattern[AnyStr]]]):
    def match(self, value: Any) -> bool:
        return bool(re.search(self.arg, value))


def any_search(value: Union[AnyStr, re.Pattern[AnyStr]]) -> Any:
    return AnySearch(value)


class AnyFullmatch(AnyRepr[Union[AnyStr, re.Pattern[AnyStr]]]):
    def match(self, value: Any) -> bool:
        return bool(re.fullmatch(self.arg, value))


def any_fullmatch(value: Union[AnyStr, re.Pattern[AnyStr]]) -> Any:
    return AnyFullmatch(value)


class AnyIn(AnyRepr[Iterable[T]]):
    def __init__(self, arg: Iterable[T]) -> None:
        self.arg: List[T] = list(arg)

    def match(self, value: Any) -> bool:
        return bool(any(a == value for a in self.arg))


def any_in(iterable: Iterable) -> Any:
    return AnyIn(iterable)
