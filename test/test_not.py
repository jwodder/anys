from typing import Any
import pytest
from anys import ANY_INT, ANY_STR, AnyFunc, AnyInstance, Not
from test_lib import assert_equal, assert_not_equal


@pytest.mark.parametrize(
    "a,value",
    [
        (ANY_STR, 42),
        (ANY_INT, "foo"),
        (AnyFunc(callable), "foo"),
        (AnyInstance((str, list)), 42),
        (42, 23),
        ("foo", "bar"),
        (None, 42),
    ],
)
def test_not_eq(a: Any, value: Any) -> None:
    assert_equal(Not(a), value)
    assert repr(Not(a)) == f"Not({a!r})"


@pytest.mark.parametrize(
    "a,value",
    [
        (ANY_STR, "foo"),
        (ANY_INT, 42),
        (AnyFunc(callable), callable),
        (AnyInstance((str, list)), "foo"),
        (AnyInstance((str, list)), [1, 2, 3]),
        (42, 42),
        ("foo", "foo"),
        (None, None),
    ],
)
def test_not_neq(a: Any, value: Any) -> None:
    assert_not_equal(Not(a), value)
