from anys import ANY_INT, AnyFunc, AnyGE, AnyLT


def test_strict_equality() -> None:
    """
    Test that various comparisons do not produce a "Non-overlapping equality
    check" error in mypy when --strict-equality is in effect
    """
    assert {"foo": ANY_INT} == {"foo": 3}
    assert {"foo": 3} == {"foo": ANY_INT}
    assert {"foo": AnyFunc(lambda n: n % 2 == 1)} == {"foo": 3}
    assert {"foo": 3} == {"foo": AnyFunc(lambda n: n % 2 == 1)}
    assert {"foo": AnyGE(1) & AnyLT(5)} == {"foo": 3}
    assert {"foo": 3} == {"foo": AnyGE(1) & AnyLT(5)}
