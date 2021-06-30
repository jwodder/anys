from typing import Any, AnyStr, Union
import pytest
from anys import AnySubstr
from test_lib import assert_equal, assert_not_equal


@pytest.mark.parametrize(
    "s,sub",
    [
        ("abc", "a"),
        ("abc", "ab"),
        ("abc", "bc"),
        (b"abc", b"a"),
        (b"abc", b"ab"),
        (b"abc", b"bc"),
        (b"abc", 97),
    ],
)
def test_any_substr_eq(s: AnyStr, sub: Union[AnyStr, int]) -> None:
    assert_equal(AnySubstr(s), sub)
    assert repr(AnySubstr(s)) == f"AnySubstr({s!r})"


@pytest.mark.parametrize(
    "s,sub",
    [
        ("abc", 97),
        (b"abc", 42),
        ("abc", b"abc"),
        (b"abc", "abc"),
        ("π", "pi"),
    ],
)
def test_any_substr_neq(s: AnyStr, sub: Any) -> None:
    assert_not_equal(AnySubstr(s), sub)
    assert repr(AnySubstr(s)) == f"AnySubstr({s!r})"
