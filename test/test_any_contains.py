from typing import Any
import pytest
from anys import ANY_FLOAT, ANY_INT, ANY_STR, AnyContains
from test_lib import assert_equal, assert_not_equal


@pytest.mark.parametrize(
    "seq,value",
    [
        ([0, 1, 2], 0),
        ([0, 1, 2], 1),
        ([0, 1, 2], 2),
        ("abc", "a"),
        ("abc", "ab"),
        (["foo", 42], "foo"),
        (["foo", 42], 42),
        (["foo", 42], ANY_STR),
        (["foo", 42], ANY_INT),
        (("foo", "bar"), "foo"),
        ({"foo", "bar"}, "foo"),
        ({"foo": 42, "bar": 23}, "foo"),
        (b"abc", 97),
    ],
)
def test_from_any_contains_eq(seq: Any, value: Any) -> None:
    assert_equal(AnyContains(value), seq)
    assert repr(AnyContains(value)) == f"AnyContains({value!r})"


@pytest.mark.parametrize(
    "seq,value",
    [
        ([0, 1, 2], 3),
        (["foo", 42], 3.14),
        (["foo", 42], ANY_FLOAT),
        (["foo", "bar"], ANY_INT),
        ([42, 23], ANY_STR),
        (("foo", "bar"), "quux"),
        ({"foo", "bar"}, "quux"),
        ({"foo": 42, "bar": 23}, 42),
        (b"abc", 65),
        (42, 42),
    ],
)
def test_from_any_contains_neq(seq: Any, value: Any) -> None:
    assert_not_equal(AnyContains(value), seq)
