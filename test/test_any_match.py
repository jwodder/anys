import re
from typing import Any, AnyStr, Pattern, Union
import pytest
from anys import any_fullmatch, any_match, any_search
from test_lib import assert_equal, assert_not_equal


@pytest.mark.parametrize(
    "rgx,value",
    [
        (r"\d+", "12345"),
        (r"\d+", "123abc"),
        (re.compile(r"\d+"), "12345"),
        (re.compile(r"\d+"), "123abc"),
        (br"\d+", b"12345"),
        (br"\d+", b"123abc"),
        (re.compile(br"\d+"), b"12345"),
        (re.compile(br"\d+"), b"123abc"),
    ],
)
def test_any_match_eq(rgx: Union[AnyStr, Pattern[AnyStr]], value: AnyStr) -> None:
    assert_equal(any_match(rgx), value)
    assert repr(any_match(rgx)) == f"AnyMatch({rgx!r})"


@pytest.mark.parametrize(
    "rgx,value",
    [
        (r"\d+", b"12345"),
        (r"\d+", b"123abc"),
        (re.compile(r"\d+"), b"12345"),
        (re.compile(r"\d+"), b"123abc"),
        (br"\d+", "12345"),
        (br"\d+", "123abc"),
        (re.compile(br"\d+"), "12345"),
        (re.compile(br"\d+"), "123abc"),
        (r"\d+", "abc123"),
        (br"\d+", b"abc123"),
        (r"\d+", 42),
        (re.compile(r"\d+"), 42),
    ],
)
def test_any_match_neq(rgx: Union[AnyStr, Pattern[AnyStr]], value: Any) -> None:
    assert_not_equal(any_match(rgx), value)


@pytest.mark.parametrize(
    "rgx,value",
    [
        (r"\d+", "12345"),
        (r"\d+", "123abc"),
        (re.compile(r"\d+"), "12345"),
        (re.compile(r"\d+"), "123abc"),
        (br"\d+", b"12345"),
        (br"\d+", b"123abc"),
        (re.compile(br"\d+"), b"12345"),
        (re.compile(br"\d+"), b"123abc"),
        (r"\d+", "abc123"),
        (br"\d+", b"abc123"),
    ],
)
def test_any_search_eq(rgx: Union[AnyStr, Pattern[AnyStr]], value: AnyStr) -> None:
    assert_equal(any_search(rgx), value)
    assert repr(any_search(rgx)) == f"AnySearch({rgx!r})"


@pytest.mark.parametrize(
    "rgx,value",
    [
        (r"\d+", b"12345"),
        (r"\d+", b"123abc"),
        (re.compile(r"\d+"), b"12345"),
        (re.compile(r"\d+"), b"123abc"),
        (br"\d+", "12345"),
        (br"\d+", "123abc"),
        (re.compile(br"\d+"), "12345"),
        (re.compile(br"\d+"), "123abc"),
        (r"\d+", 42),
        (re.compile(r"\d+"), 42),
    ],
)
def test_any_search_neq(rgx: Union[AnyStr, Pattern[AnyStr]], value: Any) -> None:
    assert_not_equal(any_search(rgx), value)


@pytest.mark.parametrize(
    "rgx,value",
    [
        (r"\d+", "12345"),
        (re.compile(r"\d+"), "12345"),
        (br"\d+", b"12345"),
        (re.compile(br"\d+"), b"12345"),
    ],
)
def test_any_fullmatch_eq(rgx: Union[AnyStr, Pattern[AnyStr]], value: AnyStr) -> None:
    assert_equal(any_fullmatch(rgx), value)
    assert repr(any_fullmatch(rgx)) == f"AnyFullmatch({rgx!r})"


@pytest.mark.parametrize(
    "rgx,value",
    [
        (r"\d+", "123abc"),
        (br"\d+", b"123abc"),
        (r"\d+", b"12345"),
        (r"\d+", b"123abc"),
        (re.compile(r"\d+"), b"12345"),
        (re.compile(r"\d+"), b"123abc"),
        (br"\d+", "12345"),
        (br"\d+", "123abc"),
        (re.compile(br"\d+"), "12345"),
        (re.compile(br"\d+"), "123abc"),
        (r"\d+", "abc123"),
        (br"\d+", b"abc123"),
        (r"\d+", 42),
        (re.compile(r"\d+"), 42),
    ],
)
def test_any_fullmatch_neq(rgx: Union[AnyStr, Pattern[AnyStr]], value: Any) -> None:
    assert_not_equal(any_fullmatch(rgx), value)
