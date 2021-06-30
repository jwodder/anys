from typing import Any
import pytest
from anys import ANY_INT, AnyGE, AnyGT, AnyLE, AnyLT
from test_lib import assert_equal, assert_not_equal


@pytest.mark.parametrize(
    "arg,value",
    [
        (42, 108),
        (42, 42),
        ("abc", "def"),
        ("abc", "abc"),
        ({"foo", 42}, {"foo", 42, 3.14}),
        ({"foo", 42}, {"foo", 42}),
    ],
)
def test_any_ge_eq(arg: Any, value: Any) -> None:
    assert_equal(AnyGE(arg), value)
    assert repr(AnyGE(arg)) == f"AnyGE({arg!r})"


@pytest.mark.parametrize(
    "arg,value",
    [
        (108, 42),
        ("def", "abc"),
        ({"foo", 42, 3.14}, {"foo", 42}),
        ({"foo"}, {42}),
        ({"foo", 42}, {42, 3.14}),
        ("1", 1),
        (ANY_INT, 23),
    ],
)
def test_any_ge_neq(arg: Any, value: Any) -> None:
    assert_not_equal(AnyGE(arg), value)


@pytest.mark.parametrize(
    "arg,value",
    [
        (42, 108),
        ("abc", "def"),
        ({"foo", 42}, {"foo", 42, 3.14}),
    ],
)
def test_any_gt_eq(arg: Any, value: Any) -> None:
    assert_equal(AnyGT(arg), value)
    assert repr(AnyGT(arg)) == f"AnyGT({arg!r})"


@pytest.mark.parametrize(
    "arg,value",
    [
        (42, 42),
        ("abc", "abc"),
        ({"foo", 42}, {"foo", 42}),
        (108, 42),
        ("def", "abc"),
        ({"foo", 42, 3.14}, {"foo", 42}),
        ({"foo"}, {42}),
        ({"foo", 42}, {42, 3.14}),
        ("1", 1),
        (ANY_INT, 23),
    ],
)
def test_any_gt_neq(arg: Any, value: Any) -> None:
    assert_not_equal(AnyGT(arg), value)


@pytest.mark.parametrize(
    "arg,value",
    [
        (108, 42),
        (42, 42),
        ("def", "abc"),
        ("abc", "abc"),
        ({"foo", 42, 31.4}, {"foo", 42}),
        ({"foo", 42}, {"foo", 42}),
    ],
)
def test_any_le_eq(arg: Any, value: Any) -> None:
    assert_equal(AnyLE(arg), value)
    assert repr(AnyLE(arg)) == f"AnyLE({arg!r})"


@pytest.mark.parametrize(
    "arg,value",
    [
        (42, 108),
        ("abc", "def"),
        ({"foo", 42}, {"foo", 42, 3.14}),
        ({"foo"}, {42}),
        ({"foo", 42}, {42, 3.14}),
        ("1", 1),
        (ANY_INT, 23),
    ],
)
def test_any_le_neq(arg: Any, value: Any) -> None:
    assert_not_equal(AnyLE(arg), value)


@pytest.mark.parametrize(
    "arg,value",
    [
        (108, 42),
        ("def", "abc"),
        ({"foo", 42, 3.14}, {"foo", 42}),
    ],
)
def test_any_lt_eq(arg: Any, value: Any) -> None:
    assert_equal(AnyLT(arg), value)
    assert repr(AnyLT(arg)) == f"AnyLT({arg!r})"


@pytest.mark.parametrize(
    "arg,value",
    [
        (42, 42),
        ("abc", "abc"),
        ({"foo", 42}, {"foo", 42}),
        (42, 108),
        ("abc", "def"),
        ({"foo", 42}, {"foo", 42, 3.14}),
        ({"foo"}, {42}),
        ({"foo", 42}, {42, 3.14}),
        ("1", 1),
        (ANY_INT, 23),
    ],
)
def test_any_lt_neq(arg: Any, value: Any) -> None:
    assert_not_equal(AnyLT(arg), value)
