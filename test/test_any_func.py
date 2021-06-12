from functools import partial
from operator import lt
from typing import Any, Callable
import pytest
from anys import any_func
from test_lib import assert_equal


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
    assert_equal(any_func(func), value)
