from collections.abc import Iterable, Mapping, Sequence
from datetime import date, datetime, time, timezone
from numbers import Number
from typing import Any
import pytest
from anys import (
    ANY_AWARE_DATETIME,
    ANY_AWARE_TIME,
    ANY_BOOL,
    ANY_BYTES,
    ANY_COMPLEX,
    ANY_DATE,
    ANY_DATETIME,
    ANY_DICT,
    ANY_FLOAT,
    ANY_INT,
    ANY_ITERABLE,
    ANY_ITERATOR,
    ANY_LIST,
    ANY_MAPPING,
    ANY_NAIVE_DATETIME,
    ANY_NAIVE_TIME,
    ANY_NUMBER,
    ANY_SEQUENCE,
    ANY_SET,
    ANY_STR,
    ANY_STRICT_DATE,
    ANY_TIME,
    ANY_TUPLE,
    AnyInstance,
    ClassInfo,
)
from test_lib import assert_equal, assert_not_equal


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
def test_any_instance_eq(classinfo: ClassInfo, value: Any) -> None:
    assert_equal(AnyInstance(classinfo), value)
    assert repr(AnyInstance(classinfo)) == f"AnyInstance({classinfo!r})"


@pytest.mark.parametrize(
    "classinfo,value",
    [
        (str, 42),
        (int, "foo"),
        (int, 3.14),
        (tuple, []),
        (list, (1, 2, 3)),
        ((str, list), 42),
        ((str, list), (1, 2, 3)),
    ],
)
def test_any_instance_neq(classinfo: ClassInfo, value: Any) -> None:
    assert_not_equal(AnyInstance(classinfo), value)
    assert repr(AnyInstance(classinfo)) == f"AnyInstance({classinfo!r})"


@pytest.mark.parametrize("value", [True, False])
def test_any_bool_eq(value: bool) -> None:
    assert_equal(ANY_BOOL, value)


@pytest.mark.parametrize("value", [None, 42, "foo", (), 3.14, [], {}])
def test_any_bool_neq(value: Any) -> None:
    assert_not_equal(ANY_BOOL, value)


def test_any_bool_repr() -> None:
    assert repr(ANY_BOOL) == "ANY_BOOL"


@pytest.mark.parametrize("value", [b"", b"foo"])
def test_any_bytes_eq(value: bytes) -> None:
    assert_equal(ANY_BYTES, value)


@pytest.mark.parametrize("value", [None, 42, (), 3.14, [], {}, "foo"])
def test_any_bytes_neq(value: Any) -> None:
    assert_not_equal(ANY_BYTES, value)


def test_any_bytes_repr() -> None:
    assert repr(ANY_BYTES) == "ANY_BYTES"


@pytest.mark.parametrize("value", [1j, 1.2j, 1 + 2j, 1.2 + 3.4j])
def test_any_complex_eq(value: complex) -> None:
    assert_equal(ANY_COMPLEX, value)


@pytest.mark.parametrize("value", [None, "foo", (), 3.14, 42, [], {}])
def test_any_complex_neq(value: Any) -> None:
    assert_not_equal(ANY_COMPLEX, value)


def test_any_complex_repr() -> None:
    assert repr(ANY_COMPLEX) == "ANY_COMPLEX"


@pytest.mark.parametrize(
    "value",
    [
        date(2021, 6, 12),
        datetime(2021, 6, 12, 18, 3, 6),
        datetime(2021, 6, 12, 18, 3, 6, tzinfo=timezone.utc),
    ],
)
def test_any_date_eq(value: date) -> None:
    assert_equal(ANY_DATE, value)


@pytest.mark.parametrize(
    "value",
    [
        time(18, 3, 6),
        timezone.utc,
        None,
        42,
        "foo",
        (),
        3.14,
        [],
        {},
        b"bytes",
        "2021-06-12",
    ],
)
def test_any_date_neq(value: Any) -> None:
    assert_not_equal(ANY_DATE, value)


def test_any_date_repr() -> None:
    assert repr(ANY_DATE) == "ANY_DATE"


@pytest.mark.parametrize(
    "value",
    [
        datetime(2021, 6, 12, 18, 3, 6),
        datetime(2021, 6, 12, 18, 3, 6, tzinfo=timezone.utc),
    ],
)
def test_any_datetime_eq(value: datetime) -> None:
    assert_equal(ANY_DATETIME, value)


@pytest.mark.parametrize(
    "value",
    [
        date(2021, 6, 12),
        time(18, 3, 6),
        timezone.utc,
        None,
        42,
        "foo",
        (),
        3.14,
        [],
        {},
        b"bytes",
        "2021-06-12T18:03:06+00:00",
    ],
)
def test_any_datetime_neq(value: Any) -> None:
    assert_not_equal(ANY_DATETIME, value)


def test_any_datetime_repr() -> None:
    assert repr(ANY_DATETIME) == "ANY_DATETIME"


@pytest.mark.parametrize("value", [{}, {"foo": "bar"}])
def test_any_dict_eq(value: dict) -> None:
    assert_equal(ANY_DICT, value)


@pytest.mark.parametrize(
    "value", [None, 42, (), 3.14, [], "foo", set(), {1, 2}, b"bar"]
)
def test_any_dict_neq(value: Any) -> None:
    assert_not_equal(ANY_DICT, value)


def test_any_dict_repr() -> None:
    assert repr(ANY_DICT) == "ANY_DICT"


@pytest.mark.parametrize(
    "value", [-2.71828, 0.0, -0.0, 3.14, float("nan"), float("-inf"), float("inf")]
)
def test_any_float_eq(value: float) -> None:
    assert_equal(ANY_FLOAT, value)


@pytest.mark.parametrize("value", [None, "foo", (), 3, 1 + 2j, 1.2 + 3.4j, [], {}])
def test_any_float_neq(value: Any) -> None:
    assert_not_equal(ANY_FLOAT, value)


def test_any_float_repr() -> None:
    assert repr(ANY_FLOAT) == "ANY_FLOAT"


@pytest.mark.parametrize("value", [-23, 0, 42, True, False])
def test_any_int_eq(value: int) -> None:
    assert_equal(ANY_INT, value)


@pytest.mark.parametrize("value", [None, "foo", (), 3.14, 1 + 2j, 1.2 + 3.4j, [], {}])
def test_any_int_neq(value: Any) -> None:
    assert_not_equal(ANY_INT, value)


def test_any_int_repr() -> None:
    assert repr(ANY_INT) == "ANY_INT"


@pytest.mark.parametrize("value", ["foo", b"bar", (), [], {}, set(), iter([])])
def test_any_iterable_eq(value: Iterable) -> None:
    assert_equal(ANY_ITERABLE, value)


@pytest.mark.parametrize("value", [42, 3.14, 1 + 2j, None])
def test_any_iterable_neq(value: Any) -> None:
    assert_not_equal(ANY_ITERABLE, value)


def test_any_iterable_repr() -> None:
    assert repr(ANY_ITERABLE) == "ANY_ITERABLE"


def test_any_iterator_eq() -> None:
    assert_equal(ANY_ITERATOR, iter([]))


@pytest.mark.parametrize(
    "value", [42, 3.14, 1 + 2j, None, "foo", b"bar", (), [], {}, set()]
)
def test_any_iterator_neq(value: Any) -> None:
    assert_not_equal(ANY_ITERATOR, value)


def test_any_iterator_repr() -> None:
    assert repr(ANY_ITERATOR) == "ANY_ITERATOR"


@pytest.mark.parametrize("value", [[], [1], [1, 2, 3]])
def test_any_list_eq(value: list) -> None:
    assert_equal(ANY_LIST, value)


@pytest.mark.parametrize("value", [None, 42, "foo", 3.14, (), {}, b"bar"])
def test_any_list_neq(value: Any) -> None:
    assert_not_equal(ANY_LIST, value)


def test_any_list_repr() -> None:
    assert repr(ANY_LIST) == "ANY_LIST"


# TODO: Add non-dict mappings
@pytest.mark.parametrize("value", [{}, {"foo": "bar"}])
def test_any_mapping_eq(value: Mapping) -> None:
    assert_equal(ANY_MAPPING, value)


@pytest.mark.parametrize(
    "value", [None, 42, (), 3.14, [], "foo", set(), {1, 2}, b"bar"]
)
def test_any_mapping_neq(value: Any) -> None:
    assert_not_equal(ANY_MAPPING, value)


def test_any_mapping_repr() -> None:
    assert repr(ANY_MAPPING) == "ANY_MAPPING"


def test_any_naive_datetime_eq() -> None:
    assert_equal(ANY_NAIVE_DATETIME, datetime(2021, 6, 12, 18, 3, 6))


@pytest.mark.parametrize(
    "value",
    [
        datetime(2021, 6, 12, 18, 3, 6, tzinfo=timezone.utc),
        date(2021, 6, 12),
        time(18, 3, 6),
        timezone.utc,
        None,
        42,
        "foo",
        (),
        3.14,
        [],
        {},
        b"bytes",
        "2021-06-12T18:03:06",
    ],
)
def test_any_naive_datetime_neq(value: Any) -> None:
    assert_not_equal(ANY_NAIVE_DATETIME, value)


def test_any_naive_datetime_repr() -> None:
    assert repr(ANY_NAIVE_DATETIME) == "ANY_NAIVE_DATETIME"


def test_any_naive_time_eq() -> None:
    assert_equal(ANY_NAIVE_TIME, time(18, 3, 6))


@pytest.mark.parametrize(
    "value",
    [
        time(18, 3, 6, tzinfo=timezone.utc),
        date(2021, 6, 12),
        datetime(2021, 6, 12, 18, 3, 6),
        datetime(2021, 6, 12, 18, 3, 6, tzinfo=timezone.utc),
        timezone.utc,
        None,
        42,
        "foo",
        (),
        3.14,
        [],
        {},
        b"bytes",
        "18:03:06",
        "18:03:06+00:00",
    ],
)
def test_any_naive_time_neq(value: Any) -> None:
    assert_not_equal(ANY_NAIVE_TIME, value)


def test_any_naive_time_repr() -> None:
    assert repr(ANY_NAIVE_TIME) == "ANY_NAIVE_TIME"


@pytest.mark.parametrize(
    "value",
    [
        0,
        42,
        -23,
        True,
        False,
        -2.71828,
        0.0,
        -0.0,
        3.14,
        float("nan"),
        float("-inf"),
        float("inf"),
        1j,
        1.2j,
        1 + 2j,
        1.2 + 3.4j,
    ],
)
def test_any_number_eq(value: Number) -> None:
    assert_equal(ANY_NUMBER, value)


@pytest.mark.parametrize("value", [None, "foo", (), [], {}, b"bar"])
def test_any_number_neq(value: Any) -> None:
    assert_not_equal(ANY_NUMBER, value)


def test_any_number_repr() -> None:
    assert repr(ANY_NUMBER) == "ANY_NUMBER"


@pytest.mark.parametrize("value", ["foo", b"bar", (), []])
def test_any_sequence_eq(value: Sequence) -> None:
    assert_equal(ANY_SEQUENCE, value)


@pytest.mark.parametrize("value", [42, 3.14, 1 + 2j, None, {}, set(), iter([])])
def test_any_sequence_neq(value: Any) -> None:
    assert_not_equal(ANY_SEQUENCE, value)


def test_any_sequence_repr() -> None:
    assert repr(ANY_SEQUENCE) == "ANY_SEQUENCE"


@pytest.mark.parametrize("value", [set(), {1}, {1, 2, 3}])
def test_any_set_eq(value: set) -> None:
    assert_equal(ANY_SET, value)


@pytest.mark.parametrize("value", [None, 42, "foo", 3.14, (), [], {}, b"bar"])
def test_any_set_neq(value: Any) -> None:
    assert_not_equal(ANY_SET, value)


def test_any_set_repr() -> None:
    assert repr(ANY_SET) == "ANY_SET"


@pytest.mark.parametrize("value", ["", "foo"])
def test_any_str_eq(value: str) -> None:
    assert_equal(ANY_STR, value)


@pytest.mark.parametrize("value", [None, 42, (), 3.14, [], {}, b"bar"])
def test_any_str_neq(value: Any) -> None:
    assert_not_equal(ANY_STR, value)


def test_any_str_repr() -> None:
    assert repr(ANY_STR) == "ANY_STR"


def test_any_strict_date_eq() -> None:
    assert_equal(ANY_STRICT_DATE, date(2021, 6, 12))


@pytest.mark.parametrize(
    "value",
    [
        datetime(2021, 6, 12, 18, 3, 6),
        datetime(2021, 6, 12, 18, 3, 6, tzinfo=timezone.utc),
        time(18, 3, 6),
        timezone.utc,
        None,
        42,
        "foo",
        (),
        3.14,
        [],
        {},
        b"bytes",
        "2021-06-12",
    ],
)
def test_any_strict_date_neq(value: Any) -> None:
    assert_not_equal(ANY_STRICT_DATE, value)


def test_any_strict_date_repr() -> None:
    assert repr(ANY_STRICT_DATE) == "ANY_STRICT_DATE"


@pytest.mark.parametrize(
    "value",
    [
        time(18, 3, 6),
        time(18, 3, 6, tzinfo=timezone.utc),
    ],
)
def test_any_time_eq(value: time) -> None:
    assert_equal(ANY_TIME, value)


@pytest.mark.parametrize(
    "value",
    [
        date(2021, 6, 12),
        datetime(2021, 6, 12, 18, 3, 6),
        datetime(2021, 6, 12, 18, 3, 6, tzinfo=timezone.utc),
        timezone.utc,
        None,
        42,
        "foo",
        (),
        3.14,
        [],
        {},
        b"bytes",
        "18:03:06",
        "18:03:06+00:00",
    ],
)
def test_any_time_neq(value: Any) -> None:
    assert_not_equal(ANY_TIME, value)


def test_any_time_repr() -> None:
    assert repr(ANY_TIME) == "ANY_TIME"


@pytest.mark.parametrize("value", [(), (1,), (1, 2, 3)])
def test_any_tuple_eq(value: tuple) -> None:
    assert_equal(ANY_TUPLE, value)


@pytest.mark.parametrize("value", [None, 42, "foo", 3.14, [], {}, b"bar"])
def test_any_tuple_neq(value: Any) -> None:
    assert_not_equal(ANY_TUPLE, value)


def test_any_tuple_repr() -> None:
    assert repr(ANY_TUPLE) == "ANY_TUPLE"


def test_any_aware_datetime_eq() -> None:
    assert_equal(
        ANY_AWARE_DATETIME, datetime(2021, 6, 12, 18, 3, 6, tzinfo=timezone.utc)
    )


@pytest.mark.parametrize(
    "value",
    [
        datetime(2021, 6, 12, 18, 3, 6),
        date(2021, 6, 12),
        time(18, 3, 6),
        timezone.utc,
        None,
        42,
        "foo",
        (),
        3.14,
        [],
        {},
        b"bytes",
        "2021-06-12T18:03:06+00:00",
    ],
)
def test_any_aware_datetime_neq(value: Any) -> None:
    assert_not_equal(ANY_AWARE_DATETIME, value)


def test_any_aware_datetime_repr() -> None:
    assert repr(ANY_AWARE_DATETIME) == "ANY_AWARE_DATETIME"


def test_any_aware_time_eq() -> None:
    assert_equal(ANY_AWARE_TIME, time(18, 3, 6, tzinfo=timezone.utc))


@pytest.mark.parametrize(
    "value",
    [
        datetime(2021, 6, 12, 18, 3, 6),
        date(2021, 6, 12),
        time(18, 3, 6),
        timezone.utc,
        None,
        42,
        "foo",
        (),
        3.14,
        [],
        {},
        b"bytes",
        "2021-06-12T18:03:06+00:00",
    ],
)
def test_any_aware_time_neq(value: Any) -> None:
    assert_not_equal(ANY_AWARE_TIME, value)


def test_any_aware_time_repr() -> None:
    assert repr(ANY_AWARE_TIME) == "ANY_AWARE_TIME"
