from typing import Any
import pytest
from anys import ANY_FALSY, ANY_TRUTHY
from test_lib import assert_equal, assert_not_equal


@pytest.mark.parametrize(
    "value",
    [
        True,
        1,
        3.14,
        1j,
        "foo",
        {"foo": 42},
        [1, 2, 3],
        {1, 2, 3},
        (1, 2, 3),
        object(),
    ],
)
def test_any_truthy_eq_any_falsy_neq(value: Any) -> None:
    assert_equal(ANY_TRUTHY, value)
    assert_not_equal(ANY_FALSY, value)


@pytest.mark.parametrize(
    "value",
    [
        None,
        False,
        0,
        0.0,
        0j,
        "",
        {},
        [],
        set(),
        (),
    ],
)
def test_any_truthy_neq_any_falsy_eq(value: Any) -> None:
    assert_not_equal(ANY_TRUTHY, value)
    assert_equal(ANY_FALSY, value)


def test_any_truthy_repr() -> None:
    assert repr(ANY_TRUTHY) == "ANY_TRUTHY"


def test_any_falsy_repr() -> None:
    assert repr(ANY_FALSY) == "ANY_FALSY"
