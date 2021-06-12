from typing import Any, Callable
import pytest
from anys import ANY_INT, ANY_STR, AnyInstance

@pytest.mark.parametrize("classinfo,value", [
    (str, "foo"),
    (int, 42),
    (tuple, ()),
    (list, [1, 2, 3]),
    ((str, list), "foo"),
    ((str, list), [1, 2, 3]),
])
def test_any_instance(classinfo: Callable, value: Any) -> None:
    a = AnyInstance(classinfo)
    assert a == value
    assert value == a
    assert {"foo": value} == {"foo": a}
    assert {"foo": a} == {"foo": value}
    assert [1, 2, value, 3] == [1, 2, a, 3]
    assert [1, 2, a, 3] == [1, 2, value, 3]


@pytest.mark.parametrize("value", ["", "foo"])
def test_any_str(value: str) -> None:
    assert ANY_STR == value
    assert value == ANY_STR
    assert {"foo": value} == {"foo": ANY_STR}
    assert {"foo": ANY_STR} == {"foo": value}
    assert [1, 2, value, 3] == [1, 2, ANY_STR, 3]
    assert [1, 2, ANY_STR, 3] == [1, 2, value, 3]


@pytest.mark.parametrize("value", [-23, 0, 42])
def test_any_int(value: int) -> None:
    assert ANY_INT == value
    assert value == ANY_INT
    assert {"foo": value} == {"foo": ANY_INT}
    assert {"foo": ANY_INT} == {"foo": value}
    assert [1, 2, value, 3] == [1, 2, ANY_INT, 3]
    assert [1, 2, ANY_INT, 3] == [1, 2, value, 3]
