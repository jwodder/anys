from datetime import date, datetime, time, timezone
from typing import Any
import pytest
from anys import (
    ANY_AWARE_DATETIME_STR,
    ANY_AWARE_TIME_STR,
    ANY_DATE_STR,
    ANY_DATETIME_STR,
    ANY_NAIVE_DATETIME_STR,
    ANY_NAIVE_TIME_STR,
    ANY_TIME_STR,
)
from test_lib import assert_equal, assert_not_equal


@pytest.mark.parametrize(
    "value",
    [
        "2021-06-24T19:40:06",
        "2021-06-24T19:40:06Z",
        "2021-06-24T19:40:06+00:00",
        "2021-06-24T19:40:06+0000",
        "2021-06-24T19:40:06+00",
        "2021-06-24T15:40:06-04:00",
        "2021-06-24T15:40:06-0400",
        "2021-06-24T15:40:06-04",
        "2021-06-24 19:40:06",
        "2021-06-24 19:40:06Z",
        "2021-06-24 19:40:06+00:00",
        "2021-06-24 19:40:06+0000",
        "2021-06-24 15:40:06-04:00",
        "2021-06-24 15:40:06-0400",
        "2021-06-24 15:40:06-04",
        "2021-06-24T19:40",
        "2021-06-24T19:40Z",
        "2021-06-24T19:40:06.1",
        "2021-06-24T19:40:06.1Z",
        "2021-06-24T19:40:06.123456",
        "2021-06-24T19:40:06.123456Z",
    ],
)
def test_any_datetime_str_eq(value: Any) -> None:
    assert_equal(ANY_DATETIME_STR, value)


@pytest.mark.parametrize(
    "value",
    [
        "2021-13-01T12:34:56Z",
        "2021-01-32T12:34:56Z",
        "2021-01-01T24:34:56Z",
        "2021-01-01T12:60:56Z",
        "2021-01-01T12:34:60Z",
        "2021-06-24",
        "12:34:56",
        "12:34:56Z",
        datetime(2021, 6, 24, 19, 40, 6),
        datetime(2021, 6, 24, 19, 40, 6, tzinfo=timezone.utc),
        1624563606,
        "1624563606",
    ],
)
def test_any_datetime_str_neq(value: Any) -> None:
    assert_not_equal(ANY_DATETIME_STR, value)


def test_any_datetime_str_repr() -> None:
    assert repr(ANY_DATETIME_STR) == "ANY_DATETIME_STR"


@pytest.mark.parametrize(
    "value",
    [
        "2021-06-24T19:40:06Z",
        "2021-06-24T19:40:06+00:00",
        "2021-06-24T19:40:06+0000",
        "2021-06-24T19:40:06+00",
        "2021-06-24T15:40:06-04:00",
        "2021-06-24T15:40:06-0400",
        "2021-06-24T15:40:06-04",
        "2021-06-24 19:40:06Z",
        "2021-06-24 19:40:06+00:00",
        "2021-06-24 19:40:06+0000",
        "2021-06-24 15:40:06-04:00",
        "2021-06-24 15:40:06-0400",
        "2021-06-24 15:40:06-04",
        "2021-06-24T19:40Z",
        "2021-06-24T19:40:06.1Z",
        "2021-06-24T19:40:06.123456Z",
    ],
)
def test_any_aware_datetime_str_eq(value: Any) -> None:
    assert_equal(ANY_AWARE_DATETIME_STR, value)


@pytest.mark.parametrize(
    "value",
    [
        "2021-06-24T19:40:06",
        "2021-06-24 19:40:06",
        "2021-13-01T12:34:56",
        "2021-01-32T12:34:56",
        "2021-01-01T24:34:56",
        "2021-01-01T12:60:56",
        "2021-01-01T12:34:60",
        "2021-06-24",
        "12:34:56",
        "12:34:56Z",
        datetime(2021, 6, 24, 19, 40, 6),
        datetime(2021, 6, 24, 19, 40, 6, tzinfo=timezone.utc),
        1624563606,
        "1624563606",
    ],
)
def test_any_aware_datetime_str_neq(value: Any) -> None:
    assert_not_equal(ANY_AWARE_DATETIME_STR, value)


def test_any_aware_datetime_str_repr() -> None:
    assert repr(ANY_AWARE_DATETIME_STR) == "ANY_AWARE_DATETIME_STR"


@pytest.mark.parametrize(
    "value",
    [
        "2021-06-24T19:40",
        "2021-06-24T19:40:06",
        "2021-06-24T19:40:06.1",
        "2021-06-24T19:40:06.123456",
    ],
)
def test_any_naive_datetime_str_eq(value: Any) -> None:
    assert_equal(ANY_NAIVE_DATETIME_STR, value)


@pytest.mark.parametrize(
    "value",
    [
        "2021-06-24T19:40:06Z",
        "2021-06-24 19:40:06Z",
        "2021-13-01T12:34:56Z",
        "2021-01-32T12:34:56Z",
        "2021-01-01T24:34:56Z",
        "2021-01-01T12:60:56Z",
        "2021-01-01T12:34:60Z",
        "2021-06-24",
        "12:34:56",
        "12:34:56Z",
        datetime(2021, 6, 24, 19, 40, 6),
        datetime(2021, 6, 24, 19, 40, 6, tzinfo=timezone.utc),
        1624563606,
        "1624563606",
    ],
)
def test_any_naive_datetime_str_neq(value: Any) -> None:
    assert_not_equal(ANY_NAIVE_DATETIME_STR, value)


def test_any_naive_datetime_str_repr() -> None:
    assert repr(ANY_NAIVE_DATETIME_STR) == "ANY_NAIVE_DATETIME_STR"


def test_any_date_str_eq() -> None:
    assert_equal(ANY_DATE_STR, "2021-06-24")


@pytest.mark.parametrize(
    "value",
    [
        "2021-06-24T19:40:06",
        "2021-06-24T19:40:06Z",
        "2021-13-01",
        "2021-01-32",
        "12:34:56",
        "12:34:56Z",
        date(2021, 6, 24),
    ],
)
def test_any_date_str_neq(value: Any) -> None:
    assert_not_equal(ANY_DATE_STR, value)


def test_any_date_str_repr() -> None:
    assert repr(ANY_DATE_STR) == "ANY_DATE_STR"


@pytest.mark.parametrize(
    "value",
    [
        "19:40:06",
        "19:40:06Z",
        "19:40:06+00:00",
        "19:40:06+0000",
        "19:40:06+00",
        "15:40:06-04:00",
        "15:40:06-0400",
        "15:40:06-04",
        "19:40",
        "19:40Z",
        "19:40:06.1",
        "19:40:06.1Z",
        "19:40:06.123456",
        "19:40:06.123456Z",
    ],
)
def test_any_time_str_eq(value: Any) -> None:
    assert_equal(ANY_TIME_STR, value)


@pytest.mark.parametrize(
    "value",
    [
        "2021-06-24T19:40:06",
        "2021-06-24T19:40:06Z",
        "24:34:56Z",
        "12:60:56Z",
        "12:34:60Z",
        "2021-06-24",
        time(19, 40, 6),
        time(19, 40, 6, tzinfo=timezone.utc),
    ],
)
def test_any_time_str_neq(value: Any) -> None:
    assert_not_equal(ANY_TIME_STR, value)


def test_any_time_str_repr() -> None:
    assert repr(ANY_TIME_STR) == "ANY_TIME_STR"


@pytest.mark.parametrize(
    "value",
    [
        "19:40Z",
        "19:40:06Z",
        "19:40:06+00:00",
        "19:40:06+0000",
        "19:40:06+00",
        "15:40:06-04:00",
        "15:40:06-0400",
        "15:40:06-04",
        "19:40:06.1Z",
        "19:40:06.123456Z",
    ],
)
def test_any_aware_time_str_eq(value: Any) -> None:
    assert_equal(ANY_AWARE_TIME_STR, value)


@pytest.mark.parametrize(
    "value",
    [
        "19:40:06",
        "2021-06-24T19:40:06",
        "2021-06-24T19:40:06Z",
        "24:34:56Z",
        "12:60:56Z",
        "12:34:60Z",
        "2021-06-24",
        time(19, 40, 6),
        time(19, 40, 6, tzinfo=timezone.utc),
    ],
)
def test_any_aware_time_str_neq(value: Any) -> None:
    assert_not_equal(ANY_AWARE_TIME_STR, value)


def test_any_aware_time_str_repr() -> None:
    assert repr(ANY_AWARE_TIME_STR) == "ANY_AWARE_TIME_STR"


@pytest.mark.parametrize(
    "value",
    [
        "19:40:06",
        "19:40:06.1",
        "19:40:06.123456",
    ],
)
def test_any_naive_time_str_eq(value: Any) -> None:
    assert_equal(ANY_NAIVE_TIME_STR, value)


@pytest.mark.parametrize(
    "value",
    [
        "19:40:06Z",
        "2021-06-24T19:40:06",
        "2021-06-24T19:40:06Z",
        "24:34:56",
        "12:60:56",
        "12:34:60",
        "2021-06-24",
        time(19, 40, 6),
        time(19, 40, 6, tzinfo=timezone.utc),
    ],
)
def test_any_naive_time_str_neq(value: Any) -> None:
    assert_not_equal(ANY_NAIVE_TIME_STR, value)


def test_any_naive_time_str_repr() -> None:
    assert repr(ANY_NAIVE_TIME_STR) == "ANY_NAIVE_TIME_STR"
