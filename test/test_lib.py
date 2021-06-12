from typing import Any


def assert_equal(a: Any, value: Any) -> None:
    assert a == value
    assert value == a
    assert {"foo": value} == {"foo": a}
    assert {"foo": a} == {"foo": value}
    assert [1, 2, value, 3] == [1, 2, a, 3]
    assert [1, 2, a, 3] == [1, 2, value, 3]


def assert_not_equal(a: Any, value: Any) -> None:
    assert a != value
    assert value != a
    assert {"foo": value} != {"foo": a}
    assert {"foo": a} != {"foo": value}
    assert [1, 2, value, 3] != [1, 2, a, 3]
    assert [1, 2, a, 3] != [1, 2, value, 3]
