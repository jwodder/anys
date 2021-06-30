from collections.abc import Mapping
from types import SimpleNamespace
from typing import Any
import pytest
from anys import ANY_INT, ANY_STR, AnyWithEntries
from test_lib import assert_equal, assert_not_equal


@pytest.mark.parametrize(
    "arg,value",
    [
        ({"foo": ANY_INT, "bar": ANY_STR}, {"foo": 42, "bar": "glarch"}),
        ({"foo": ANY_INT, "bar": ANY_STR}, {"foo": 42, "bar": "glarch", "quux": 3.14}),
        ({}, {}),
        ({}, {"foo": 42, "bar": "glarch"}),
        ({"foo": ANY_INT, "bar": "glarch"}, {"foo": 42, "bar": "glarch"}),
        ({"foo": 42, "bar": "glarch"}, {"foo": 42, "bar": "glarch"}),
        ({1: ANY_INT, 2: ANY_STR}, [3.14, 42, "glarch"]),
    ],
)
def test_any_with_entries_eq(arg: Mapping, value: Any) -> None:
    assert_equal(AnyWithEntries(arg), value)
    assert repr(AnyWithEntries(arg)) == f"AnyWithEntries({arg!r})"


@pytest.mark.parametrize(
    "arg,value",
    [
        ({"foo": ANY_INT, "bar": ANY_STR}, {"foo": 42}),
        ({"foo": ANY_INT, "bar": ANY_STR}, {"foo": 42, "bar": 23}),
        ({"foo": ANY_INT, "bar": ANY_STR}, {}),
        ({"foo": 42, "bar": "glarch"}, {}),
        ({"foo": ANY_INT, "bar": ANY_STR}, 42),
        ({"1": ANY_INT}, [42, 23]),
        ({1: ANY_STR}, [42, 23]),
        ({5: ANY_STR}, [42, 23]),
        ({"foo": ANY_INT, "bar": ANY_STR}, SimpleNamespace(foo=42, bar="glarch")),
    ],
)
def test_any_with_entries_neq(arg: Mapping, value: Any) -> None:
    assert_not_equal(AnyWithEntries(arg), value)
