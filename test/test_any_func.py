from functools import partial
from operator import lt
from typing import Any, Callable
import pytest
from anys import AnyFunc


@pytest.mark.parametrize(
    "func,value",
    [
        (lambda x: x < 5, 4),
        (lambda x, y="foo": x in y, "oo"),
        (callable, callable),
        (len, "foo"),
        (len, [1, 2, 3]),
        (partial(lt, 5), 42),
    ],
)
def test_any_func_matches(func: Callable, value: Any) -> None:
    a = AnyFunc(func)
    assert a == value
    assert value == a
    assert {"foo": value} == {"foo": a}
    assert {"foo": a} == {"foo": value}
    assert [1, 2, value, 3] == [1, 2, a, 3]
    assert [1, 2, a, 3] == [1, 2, value, 3]
