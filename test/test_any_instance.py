from typing import Any
import pytest
from anys import ANY_INT, ANY_STR, ClassInfo, any_instance
from test_lib import assert_equal, assert_not_equal


@pytest.mark.parametrize(
    "classinfo,value",
    [
        (str, "foo"),
        (int, 42),
        (tuple, ()),
        (list, [1, 2, 3]),
        ((str, list), "foo"),
        ((str, list), [1, 2, 3]),
    ],
)
def test_any_instance_eq(classinfo: ClassInfo, value: Any) -> None:
    assert_equal(any_instance(classinfo), value)


@pytest.mark.parametrize(
    "classinfo,value",
    [
        (str, 42),
        (int, "foo"),
        (int, 3.14),
        (tuple, []),
        (list, (1, 2, 3)),
        ((str, list), 42),
        ((str, list), (1, 2, 3)),
    ],
)
def test_any_instance_neq(classinfo: ClassInfo, value: Any) -> None:
    assert_not_equal(any_instance(classinfo), value)


@pytest.mark.parametrize("value", ["", "foo"])
def test_any_str_eq(value: str) -> None:
    assert_equal(ANY_STR, value)


@pytest.mark.parametrize("value", [42, (), 3.14, [], {}])
def test_any_str_neq(value: str) -> None:
    assert_not_equal(ANY_STR, value)


@pytest.mark.parametrize("value", [-23, 0, 42])
def test_any_int_eq(value: int) -> None:
    assert_equal(ANY_INT, value)


@pytest.mark.parametrize("value", ["foo", (), 3.14, [], {}])
def test_any_int_neq(value: int) -> None:
    assert_not_equal(ANY_INT, value)
