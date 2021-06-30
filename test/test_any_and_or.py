from typing import Any, Union
import pytest
from anys import (
    ANY_FLOAT,
    ANY_INT,
    ANY_LIST,
    ANY_STR,
    AnyAnd,
    AnyFunc,
    AnyGT,
    AnyLT,
    AnyOr,
)
from test_lib import assert_equal, assert_not_equal


@pytest.mark.parametrize("value", [-23, 0, 42, True, False, "", "foo"])
def test_any_int_or_str_eq(value: Union[int, str]) -> None:
    assert_equal(ANY_INT | ANY_STR, value)


@pytest.mark.parametrize("value", [None, (), 3.14, 1 + 2j, 1.2 + 3.4j, [], {}, b"bar"])
def test_any_int_or_str_neq(value: Any) -> None:
    assert_not_equal(ANY_INT | ANY_STR, value)


def test_any_int_or_str_repr() -> None:
    assert repr(ANY_INT | ANY_STR) == "AnyOr(ANY_INT, ANY_STR)"


def test_or() -> None:
    a = ANY_INT | ANY_STR
    assert isinstance(a, AnyOr)
    assert len(a.args) == 2
    assert a.args[0] is ANY_INT
    assert a.args[1] is ANY_STR


def test_or3() -> None:
    a = ANY_INT | ANY_STR | ANY_FLOAT
    assert isinstance(a, AnyOr)
    assert len(a.args) == 3
    assert a.args[0] is ANY_INT
    assert a.args[1] is ANY_STR
    assert a.args[2] is ANY_FLOAT


def test_or_or() -> None:
    a1 = ANY_INT | ANY_FLOAT
    a2 = ANY_STR | ANY_LIST
    a = a1 | a2
    assert len(a.args) == 4
    assert a.args[0] is ANY_INT
    assert a.args[1] is ANY_FLOAT
    assert a.args[2] is ANY_STR
    assert a.args[3] is ANY_LIST


@pytest.mark.parametrize("value", [24, 30, 32.5, 41])
def test_any_gt_and_any_lt_eq(value: Union[int, float]) -> None:
    assert_equal(AnyGT(23) & AnyLT(42), value)


@pytest.mark.parametrize(
    "value", [22, 23, 42, 43, None, (), 3.14, 1 + 2j, 1.2 + 3.4j, [], {}, "foo", b"bar"]
)
def test_any_gt_and_any_lt_neq(value: Any) -> None:
    assert_not_equal(AnyGT(23) & AnyLT(42), value)


def test_any_gt_and_any_lt_repr() -> None:
    assert repr(AnyGT(23) & AnyLT(42)) == "AnyAnd(AnyGT(23), AnyLT(42))"


def test_and() -> None:
    a1 = AnyGT(23)
    a2 = AnyLT(42)
    a = a1 & a2
    assert isinstance(a, AnyAnd)
    assert len(a.args) == 2
    assert a.args[0] is a1
    assert a.args[1] is a2


def test_and3() -> None:
    a1 = AnyGT(23)
    a2 = AnyLT(42)
    a = a1 & a2 & ANY_INT
    assert isinstance(a, AnyAnd)
    assert len(a.args) == 3
    assert a.args[0] is a1
    assert a.args[1] is a2
    assert a.args[2] is ANY_INT


def test_and_and() -> None:
    a1 = AnyGT(23)
    a2 = AnyLT(42)
    a3 = ANY_INT
    a4 = AnyFunc(lambda n: n % 2 == 1)
    a = (a1 & a2) & (a3 & a4)
    assert isinstance(a, AnyAnd)
    assert len(a.args) == 4
    assert a.args[0] is a1
    assert a.args[1] is a2
    assert a.args[2] is a3
    assert a.args[3] is a4
    assert a == 31
    assert a != 30
    assert a != 31.0
    assert a != 23
    assert a != 42
