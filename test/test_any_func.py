from functools import partial
from operator import lt
from typing import Any, Callable
import pytest
from anys import AnyFunc
from test_lib import assert_equal, assert_not_equal


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
def test_any_func_eq(func: Callable, value: Any) -> None:
    assert_equal(AnyFunc(func), value)
    assert repr(AnyFunc(func)) == f"AnyFunc({func!r})"


@pytest.mark.parametrize(
    "func,value",
    [
        (lambda x: x < 5, 42),
        (lambda x, y="foo": x in y, "bar"),
        (callable, 42),
        (len, ""),
        (len, []),
        (partial(lt, 5), -5),
        (len, 42),
        (lambda x, y="foo": x in y, 42),
        (partial(lt, 5), "foo"),
    ],
)
def test_any_func_neq(func: Callable, value: Any) -> None:
    assert_not_equal(AnyFunc(func), value)
    assert repr(AnyFunc(func)) == f"AnyFunc({func!r})"
