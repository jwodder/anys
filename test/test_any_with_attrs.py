from collections.abc import Mapping
from types import SimpleNamespace
from typing import Any
import pytest
from anys import ANY_INT, ANY_STR, any_with_attrs
from test_lib import assert_equal, assert_not_equal


@pytest.mark.parametrize(
    "arg,value",
    [
        ({"foo": ANY_INT, "bar": ANY_STR}, SimpleNamespace(foo=42, bar="glarch")),
        (
            {"foo": ANY_INT, "bar": ANY_STR},
            SimpleNamespace(foo=42, bar="glarch", quux=3.14),
        ),
        ({}, SimpleNamespace()),
        ({}, SimpleNamespace(foo=42, bar="glarch")),
        ({"foo": ANY_INT, "bar": "glarch"}, SimpleNamespace(foo=42, bar="glarch")),
        ({"foo": 42, "bar": "glarch"}, SimpleNamespace(foo=42, bar="glarch")),
    ],
)
def test_any_with_attrs_eq(arg: Mapping, value: Any) -> None:
    assert_equal(any_with_attrs(arg), value)
    assert repr(any_with_attrs(arg)) == f"AnyWithAttrs({arg!r})"


@pytest.mark.parametrize(
    "arg,value",
    [
        ({"foo": ANY_INT, "bar": ANY_STR}, SimpleNamespace(foo=42)),
        ({"foo": ANY_INT, "bar": ANY_STR}, SimpleNamespace(foo=42, bar=23)),
        ({"foo": ANY_INT, "bar": ANY_STR}, SimpleNamespace()),
        ({"foo": 42, "bar": "glarch"}, SimpleNamespace()),
        ({"foo": ANY_INT, "bar": ANY_STR}, 42),
        ({1: ANY_INT}, [42, 23]),
        ({"foo": ANY_INT, "bar": ANY_STR}, {"foo": 42, "bar": "glarch"}),
    ],
)
def test_any_with_attrs_neq(arg: Mapping, value: Any) -> None:
    assert_not_equal(any_with_attrs(arg), value)
