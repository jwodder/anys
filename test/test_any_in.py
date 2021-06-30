from collections.abc import Iterable
from typing import Any
import pytest
from anys import ANY_INT, ANY_STR, AnyIn
from test_lib import assert_equal, assert_not_equal


@pytest.mark.parametrize(
    "seq,value",
    [
        ([0, 1, 2], 0),
        ([0, 1, 2], 1),
        ([0, 1, 2], 2),
        ("abc", "a"),
        ([ANY_STR, ANY_INT], "foo"),
        ([ANY_STR, ANY_INT], 42),
        ([ANY_INT, "π"], 42),
        ([ANY_INT, "π"], "π"),
        (("foo", "bar"), "foo"),
        ({"foo", "bar"}, "foo"),
        ({"foo": 42, "bar": 23}, "foo"),
        (b"abc", 97),
    ],
)
def test_from_any_in_eq(seq: Iterable, value: Any) -> None:
    assert_equal(AnyIn(seq), value)
    assert repr(AnyIn(seq)) == f"AnyIn({list(seq)})"


@pytest.mark.parametrize(
    "seq,value",
    [
        ([0, 1, 2], 3),
        ("abc", "ab"),
        ([ANY_STR, ANY_INT], 3.14),
        ([ANY_INT, "π"], "pi"),
        (("foo", "bar"), "quux"),
        ({"foo", "bar"}, "quux"),
        ({"foo": 42, "bar": 23}, 42),
        (b"abc", 65),
    ],
)
def test_from_any_in_neq(seq: Iterable, value: Any) -> None:
    assert_not_equal(AnyIn(seq), value)
