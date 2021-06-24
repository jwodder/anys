from typing import Any
import pytest
from anys import ANY_INT, any_ge, any_gt, any_le, any_lt
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
    assert_equal(any_ge(arg), value)
    assert repr(any_ge(arg)) == f"AnyGE({arg!r})"


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
    assert_not_equal(any_ge(arg), value)


@pytest.mark.parametrize(
    "arg,value",
    [
        (42, 108),
        ("abc", "def"),
        ({"foo", 42}, {"foo", 42, 3.14}),
    ],
)
def test_any_gt_eq(arg: Any, value: Any) -> None:
    assert_equal(any_gt(arg), value)
    assert repr(any_gt(arg)) == f"AnyGT({arg!r})"


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
    assert_not_equal(any_gt(arg), value)


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
    assert_equal(any_le(arg), value)
    assert repr(any_le(arg)) == f"AnyLE({arg!r})"


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
    assert_not_equal(any_le(arg), value)


@pytest.mark.parametrize(
    "arg,value",
    [
        (108, 42),
        ("def", "abc"),
        ({"foo", 42, 3.14}, {"foo", 42}),
    ],
)
def test_any_lt_eq(arg: Any, value: Any) -> None:
    assert_equal(any_lt(arg), value)
    assert repr(any_lt(arg)) == f"AnyLT({arg!r})"


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
    assert_not_equal(any_lt(arg), value)
