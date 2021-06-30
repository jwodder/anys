import re
from typing import Any, AnyStr, Pattern, Union
import pytest
from anys import AnyFullmatch, AnyMatch, AnySearch
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
    assert_equal(AnyMatch(rgx), value)
    assert repr(AnyMatch(rgx)) == f"AnyMatch({rgx!r})"


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
    assert_not_equal(AnyMatch(rgx), value)


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
    assert_equal(AnySearch(rgx), value)
    assert repr(AnySearch(rgx)) == f"AnySearch({rgx!r})"


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
    assert_not_equal(AnySearch(rgx), value)


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
    assert_equal(AnyFullmatch(rgx), value)
    assert repr(AnyFullmatch(rgx)) == f"AnyFullmatch({rgx!r})"


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
    assert_not_equal(AnyFullmatch(rgx), value)
