"""
Matchers for pytest

``anys`` provides matchers for pytest_-style assertions.  What's a "matcher,"
you say?  Well, say you're writing a unit test and you want to assert that a
given object contains the correct values.  Normally, you'd just write:

.. code:: python

    assert foo == {
        "widgets": 42,
        "name": "Alice",
        "subfoo": {
            "created_at": "2021-06-24T18:41:59Z",
            "name": "Bob",
            "widgets": 23,
        }
    }

But wait!  What if the value of ``foo["subfoo"]["created_at"]`` can't be
determined in advance, but you still need to check that it's a valid timestamp?
You'd have to compare everything in ``foo`` other than that one field to the
expected values and then separately check the timestamp field for validity.
This is where matchers come in: they're magic objects that compare equal to any
& all values that meet given criteria.  For the case above, ``anys`` allows you
to just write:

.. code:: python

    from anys import ANY_DATETIME_STR

    assert foo == {
        "widgets": 42,
        "name": "Alice",
        "subfoo": {
            "created_at": ANY_DATETIME_STR,
            "name": "Bob",
            "widgets": 23,
        }
    }

and the assertion will do what you mean.

.. _pytest: https://docs.pytest.org

Visit <https://github.com/jwodder/anys> for more information.
"""

__version__ = "0.1.0"
__author__ = "John Thorvald Wodder II"
__author_email__ = "anys@varonathe.org"
__license__ = "MIT"
__url__ = "https://github.com/jwodder/anys"

from abc import ABC, abstractmethod
from collections import abc
from datetime import date, datetime, time
from numbers import Number
import operator
import re
import sys
import types
from typing import (
    Any,
    AnyStr,
    Callable,
    Generic,
    Iterable,
    List,
    Mapping,
    Optional,
    Pattern,
    Tuple,
    TypeVar,
    Union,
)

T = TypeVar("T")

if sys.version_info[:2] >= (3, 10):
    ClassInfo = Union[
        type, types.Union, Tuple[Union[type, types.Union, Tuple[Any, ...]], ...]
    ]
else:
    ClassInfo = Union[type, Tuple[Union[type, Tuple[Any, ...]], ...]]

__all__ = [
    "ANY_AWARE_DATETIME",
    "ANY_AWARE_DATETIME_STR",
    "ANY_AWARE_TIME",
    "ANY_AWARE_TIME_STR",
    "ANY_BOOL",
    "ANY_BYTES",
    "ANY_COMPLEX",
    "ANY_DATE",
    "ANY_DATETIME",
    "ANY_DATETIME_STR",
    "ANY_DATE_STR",
    "ANY_DICT",
    "ANY_FALSY",
    "ANY_FLOAT",
    "ANY_INT",
    "ANY_ITERABLE",
    "ANY_ITERATOR",
    "ANY_LIST",
    "ANY_MAPPING",
    "ANY_NAIVE_DATETIME",
    "ANY_NAIVE_DATETIME_STR",
    "ANY_NAIVE_TIME",
    "ANY_NAIVE_TIME_STR",
    "ANY_NUMBER",
    "ANY_SEQUENCE",
    "ANY_SET",
    "ANY_STR",
    "ANY_STRICT_DATE",
    "ANY_TIME",
    "ANY_TIME_STR",
    "ANY_TRUTHY",
    "ANY_TUPLE",
    "any_contains",
    "any_fullmatch",
    "any_func",
    "any_ge",
    "any_gt",
    "any_in",
    "any_instance",
    "any_le",
    "any_lt",
    "any_match",
    "any_search",
    "any_substr",
    "any_with_attrs",
    "any_with_entries",
    "maybe",
    "not_",
]


class AnyBase(ABC):
    @abstractmethod
    def match(self, value: Any) -> bool:
        ...

    def __eq__(self, other: Any) -> bool:
        try:
            return self.match(other)
        except (TypeError, ValueError):
            return False

    def __and__(self, other: Any) -> Any:
        if isinstance(other, AnyBase):
            parts: List[AnyBase] = []
            for s in [self, other]:
                if isinstance(s, AnyAnd):
                    parts.extend(s.args)
                else:
                    parts.append(s)
            return AnyAnd(*parts)
        else:
            return NotImplemented  # pragma: no cover

    def __or__(self, other: Any) -> Any:
        if isinstance(other, AnyBase):
            parts: List[AnyBase] = []
            for s in [self, other]:
                if isinstance(s, AnyOr):
                    parts.extend(s.args)
                else:
                    parts.append(s)
            return AnyOr(*parts)
        else:
            return NotImplemented  # pragma: no cover


class AnyArg(AnyBase, Generic[T]):
    def __init__(self, arg: T, *, name: Optional[str] = None) -> None:
        self.arg = arg
        self.name = name

    def __repr__(self) -> str:
        if self.name is not None:
            return self.name
        else:
            return f"{type(self).__name__}({self.arg!r})"


class AnyFunc(AnyArg[Callable]):
    def match(self, value: Any) -> bool:
        return bool(self.arg(value))


# Anys need to be constructed via functions that return typing.Any so that
# comparing them against values with more restrictive types doesn't trigger a
# "comparison-overlap" type error in mypy.


def any_func(func: Callable) -> Any:
    """
    Returns a matcher that matches any value ``x`` for which ``func(x)`` is
    true.  If ``func(x)`` raises a `TypeError` or `ValueError`, it will be
    suppressed, and ``x == any_func(func)`` will evaluate to `False`.  All
    other exceptions are propagated out.
    """
    return AnyFunc(func)


class AnyInstance(AnyArg[ClassInfo]):
    def match(self, value: Any) -> bool:
        return isinstance(value, self.arg)


def any_instance(classinfo: ClassInfo, *, name: Optional[str] = None) -> Any:
    """
    Returns a matcher that matches any value that is an instance of
    ``classinfo``.  ``classinfo`` can be either a type or a tuple of types (or,
    starting in Python 3.10, a `Union` of types).
    """
    return AnyInstance(classinfo, name=name)


ANY_BOOL = any_instance(bool, name="ANY_BOOL")
ANY_BYTES = any_instance(bytes, name="ANY_BYTES")
ANY_COMPLEX = any_instance(complex, name="ANY_COMPLEX")
ANY_DATE = any_instance(date, name="ANY_DATE")
ANY_DATETIME = any_instance(datetime, name="ANY_DATETIME")
ANY_DICT = any_instance(dict, name="ANY_DICT")
ANY_FLOAT = any_instance(float, name="ANY_FLOAT")
ANY_INT = any_instance(int, name="ANY_INT")
ANY_ITERABLE = any_instance(abc.Iterable, name="ANY_ITERABLE")
ANY_ITERATOR = any_instance(abc.Iterator, name="ANY_ITERATOR")
ANY_LIST = any_instance(list, name="ANY_LIST")
ANY_MAPPING = any_instance(abc.Mapping, name="ANY_MAPPING")
ANY_NUMBER = any_instance(Number, name="ANY_NUMBER")
ANY_SEQUENCE = any_instance(abc.Sequence, name="ANY_SEQUENCE")
ANY_SET = any_instance(set, name="ANY_SET")
ANY_STR = any_instance(str, name="ANY_STR")
ANY_TIME = any_instance(time, name="ANY_TIME")
ANY_TUPLE = any_instance(tuple, name="ANY_TUPLE")


class AnyStrictDate(AnyBase):
    def match(self, value: Any) -> bool:
        return isinstance(value, date) and not isinstance(value, datetime)

    def __repr__(self) -> str:
        return "ANY_STRICT_DATE"


ANY_STRICT_DATE: Any = AnyStrictDate()


class AnyAwareDatetime(AnyBase):
    def match(self, value: Any) -> bool:
        return isinstance(value, datetime) and value.tzinfo is not None

    def __repr__(self) -> str:
        return "ANY_AWARE_DATETIME"


ANY_AWARE_DATETIME: Any = AnyAwareDatetime()


class AnyNaiveDatetime(AnyBase):
    def match(self, value: Any) -> bool:
        return isinstance(value, datetime) and value.tzinfo is None

    def __repr__(self) -> str:
        return "ANY_NAIVE_DATETIME"


ANY_NAIVE_DATETIME: Any = AnyNaiveDatetime()


class AnyAwareTime(AnyBase):
    def match(self, value: Any) -> bool:
        return isinstance(value, time) and value.tzinfo is not None

    def __repr__(self) -> str:
        return "ANY_AWARE_TIME"


ANY_AWARE_TIME: Any = AnyAwareTime()


class AnyNaiveTime(AnyBase):
    def match(self, value: Any) -> bool:
        return isinstance(value, time) and value.tzinfo is None

    def __repr__(self) -> str:
        return "ANY_NAIVE_TIME"


ANY_NAIVE_TIME: Any = AnyNaiveTime()


class Maybe(AnyArg[Any]):
    def match(self, value: Any) -> bool:
        return bool(value is None or self.arg == value)


def maybe(arg: Any) -> Any:
    """
    Returns a matcher that matches `None` and any value that equals or matches
    ``arg`` (which can be an `anys` matcher)
    """
    return Maybe(arg)


class Not(AnyArg[Any]):
    def match(self, value: Any) -> bool:
        return bool(self.arg != value)


def not_(arg: Any) -> Any:
    """
    Returns a matcher that matches anything that does not equal or match
    ``arg`` (which can be an `anys` matcher)
    """
    return Not(arg)


class AnyMatch(AnyArg[Union[AnyStr, Pattern[AnyStr]]]):
    def match(self, value: Any) -> bool:
        return bool(re.match(self.arg, value))


def any_match(patten: Union[AnyStr, Pattern[AnyStr]]) -> Any:
    """
    Returns a matcher that matches any string ``s`` for which
    ``re.match(pattern, s)`` succeeds
    """
    return AnyMatch(patten)


class AnySearch(AnyArg[Union[AnyStr, Pattern[AnyStr]]]):
    def match(self, value: Any) -> bool:
        return bool(re.search(self.arg, value))


def any_search(pattern: Union[AnyStr, Pattern[AnyStr]]) -> Any:
    """
    Returns a matcher that matches any string ``s`` for which
    ``re.search(pattern, s)`` succeeds
    """
    return AnySearch(pattern)


class AnyFullmatch(AnyArg[Union[AnyStr, Pattern[AnyStr]]]):
    def match(self, value: Any) -> bool:
        return bool(re.fullmatch(self.arg, value))


def any_fullmatch(
    pattern: Union[AnyStr, Pattern[AnyStr]], *, name: Optional[str] = None
) -> Any:
    """
    Returns a matcher that matches any string ``s`` for which
    ``re.fullmatch(pattern, s)`` succeeds
    """
    return AnyFullmatch(pattern, name=name)


class AnyIn(AnyArg[Iterable[T]]):
    def __init__(self, arg: Iterable[T], *, name: Optional[str] = None) -> None:
        self.arg: List[T] = list(arg)
        self.name = name

    def match(self, value: Any) -> bool:
        return bool(any(a == value for a in self.arg))


def any_in(iterable: Iterable) -> Any:
    """
    Returns a matcher that matches any value that equals or matches an element
    of ``iterable`` (which may contain `anys` matchers).  Note that, if
    ``iterable`` is a string, only individual characters in the string will
    match; to match substrings, use `any_substr()` instead.
    """
    return AnyIn(iterable)


class AnySubstr(AnyArg[AnyStr]):
    def match(self, value: Any) -> bool:
        return bool(value in self.arg)


def any_substr(s: AnyStr) -> Any:
    """Returns a matcher that matches any substring of ``s``"""
    return AnySubstr(s)


class AnyContains(AnyArg[Any]):
    def match(self, value: Any) -> bool:
        if isinstance(self.arg, AnyBase):
            return bool(any(self.arg == v for v in value))
        else:
            return bool(self.arg in value)


def any_contains(key: Any) -> Any:
    """
    Returns a matcher that matches any value for which ``key in value`` is
    true.  If ``key`` is an `anys` matcher, ``value == any_contains(key)``
    will instead be evaluated by iterating through the elements of ``value``
    and checking whether any match ``key``.
    """
    return AnyContains(key)


class AnyWithEntries(AnyArg[Mapping]):
    def match(self, value: Any) -> bool:
        for k, v in self.arg.items():
            try:
                if v != value[k]:
                    return False
            except LookupError:
                return False
        return True


def any_with_entries(mapping: Mapping) -> Any:
    """
    Returns a matcher that matches any object ``obj`` such that ``obj[k] == v``
    for all ``k,v`` in ``mapping.items()``.

    The values (but not the keys) of ``mapping`` can be `anys` matchers.
    """
    return AnyWithEntries(mapping)


class AnyWithAttrs(AnyArg[Mapping]):
    def match(self, value: Any) -> bool:
        for k, v in self.arg.items():
            try:
                if v != getattr(value, k):
                    return False
            except AttributeError:
                return False
        return True


def any_with_attrs(mapping: Mapping) -> Any:
    """
    Returns a matcher that matches any object ``obj`` such that ``getattr(obj,
    k) == v`` for all ``k,v`` in ``mapping.items()``.

    The values (but not the keys) of ``mapping`` can be `anys` matchers.
    """
    return AnyWithAttrs(mapping)


class AnyLT(AnyArg[Any]):
    def match(self, value: Any) -> bool:
        return bool(value < self.arg)


def any_lt(bound: Any) -> Any:
    """Returns a matcher that matches any value less than ``bound``"""
    return AnyLT(bound)


class AnyLE(AnyArg[Any]):
    def match(self, value: Any) -> bool:
        return bool(value <= self.arg)


def any_le(bound: Any) -> Any:
    """
    Returns a matcher that matches any value less than or equal to ``bound``
    """
    return AnyLE(bound)


class AnyGT(AnyArg[Any]):
    def match(self, value: Any) -> bool:
        return bool(value > self.arg)


def any_gt(bound: Any) -> Any:
    """Returns a matcher that matches any value greater than ``bound``"""
    return AnyGT(bound)


class AnyGE(AnyArg[Any]):
    def match(self, value: Any) -> bool:
        return bool(value >= self.arg)


def any_ge(bound: Any) -> Any:
    """
    Returns a matcher that matches any value greater than or equal to ``bound``
    """
    return AnyGE(bound)


ANY_TRUTHY = AnyFunc(bool, name="ANY_TRUTHY")
ANY_FALSY = AnyFunc(operator.not_, name="ANY_FALSY")


DATE_RGX = r"[0-9]{4,}-(?:0[1-9]|1[012])-(?:0[1-9]|[12][0-9]|3[01])"
TIME_RGX = r"(?:[01][0-9]|2[0-3]):[0-5][0-9](?::[0-5][0-9](?:\.[0-9]+)?)?"
TZ_RGX = r"(?:Z|[-+][0-9]{2}(?::?[0-9]{2})?)"

ANY_DATETIME_STR = any_fullmatch(
    re.compile(f"{DATE_RGX}[T ]{TIME_RGX}(?:{TZ_RGX})?"), name="ANY_DATETIME_STR"
)
ANY_AWARE_DATETIME_STR = any_fullmatch(
    re.compile(f"{DATE_RGX}[T ]{TIME_RGX}{TZ_RGX}"), name="ANY_AWARE_DATETIME_STR"
)
ANY_NAIVE_DATETIME_STR = any_fullmatch(
    re.compile(f"{DATE_RGX}[T ]{TIME_RGX}"), name="ANY_NAIVE_DATETIME_STR"
)

ANY_DATE_STR = any_fullmatch(re.compile(DATE_RGX), name="ANY_DATE_STR")

ANY_TIME_STR = any_fullmatch(
    re.compile(f"{TIME_RGX}(?:{TZ_RGX})?"), name="ANY_TIME_STR"
)
ANY_AWARE_TIME_STR = any_fullmatch(
    re.compile(f"{TIME_RGX}{TZ_RGX}"), name="ANY_AWARE_TIME_STR"
)
ANY_NAIVE_TIME_STR = any_fullmatch(re.compile(TIME_RGX), name="ANY_NAIVE_TIME_STR")


class AnyArgs(AnyBase):
    def __init__(self, *args: AnyBase, name: Optional[str] = None) -> None:
        self.args: List[AnyBase] = list(args)
        self.name = name

    def __repr__(self) -> str:
        return "{}({})".format(type(self).__name__, ", ".join(map(repr, self.args)))


class AnyAnd(AnyArgs):
    def match(self, value: Any) -> bool:
        return bool(all(a == value for a in self.args))


class AnyOr(AnyArgs):
    def match(self, value: Any) -> bool:
        return bool(any(a == value for a in self.args))
