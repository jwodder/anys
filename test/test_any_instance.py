from typing import Any
import pytest
from anys import ANY_INT, ANY_STR, ClassInfo, any_instance
from test_lib import assert_equal


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
def test_any_instance(classinfo: ClassInfo, value: Any) -> None:
    assert_equal(any_instance(classinfo), value)


@pytest.mark.parametrize("value", ["", "foo"])
def test_any_str(value: str) -> None:
    assert_equal(ANY_STR, value)


@pytest.mark.parametrize("value", [-23, 0, 42])
def test_any_int(value: int) -> None:
    assert_equal(ANY_INT, value)
