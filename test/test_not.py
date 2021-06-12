from typing import Any
import pytest
from anys import ANY_INT, ANY_STR, any_func, any_instance, not_
from test_lib import assert_equal, assert_not_equal


@pytest.mark.parametrize(
    "a,value",
    [
        (ANY_STR, 42),
        (ANY_INT, "foo"),
        (any_func(callable), "foo"),
        (any_instance((str, list)), 42),
        (42, 23),
        ("foo", "bar"),
        (None, 42),
    ],
)
def test_not_eq(a: Any, value: Any) -> None:
    assert_equal(not_(a), value)
    assert repr(not_(a)) == f"Not({a!r})"


@pytest.mark.parametrize(
    "a,value",
    [
        (ANY_STR, "foo"),
        (ANY_INT, 42),
        (any_func(callable), callable),
        (any_instance((str, list)), "foo"),
        (any_instance((str, list)), [1, 2, 3]),
        (42, 42),
        ("foo", "foo"),
        (None, None),
    ],
)
def test_not_neq(a: Any, value: Any) -> None:
    assert_not_equal(not_(a), value)
