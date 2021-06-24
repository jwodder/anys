.. image:: http://www.repostatus.org/badges/latest/active.svg
    :target: http://www.repostatus.org/#active
    :alt: Project Status: Active — The project has reached a stable, usable
          state and is being actively developed.

.. image:: https://github.com/jwodder/anys/workflows/Test/badge.svg?branch=master
    :target: https://github.com/jwodder/anys/actions?workflow=Test
    :alt: CI Status

.. image:: https://codecov.io/gh/jwodder/anys/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/jwodder/anys

.. image:: https://img.shields.io/pypi/pyversions/anys.svg
    :target: https://pypi.org/project/anys/

.. image:: https://img.shields.io/github/license/jwodder/anys.svg
    :target: https://opensource.org/licenses/MIT
    :alt: MIT License

`GitHub <https://github.com/jwodder/anys>`_
| `PyPI <https://pypi.org/project/anys/>`_
| `Issues <https://github.com/jwodder/anys/issues>`_

``anys`` provides matchers for pytest_-style assertions.  What's a "matcher,"
you say?  Well, say you're writing a unit test and you want to assert that a
given object contains the correct values.  Normally, you'd just write:

.. code:: python

    assert foo == {
        "widgets": 42,
        "name": "Alice",
        "subfoo": {
            "created_at": "2021-06-24T18:41:59Z",
            "name": "Bob",
            "widgets": 23,
        }
    }

But wait!  What if the value of ``foo["subfoo"]["created_at"]`` can't be
determined in advance, but you still need to check that it's a valid timestamp?
You'd have to compare everything in ``foo`` other than that one field to the
expected values and then separately check the timestamp field for validity.
This is where matchers come in: they're magic objects that compare equal to any
& all values that meet given criteria.  For the case above, ``anys`` allows you
to just write:

.. code:: python

    from anys import ANY_DATETIME_STR

    assert foo == {
        "widgets": 42,
        "name": "Alice",
        "subfoo": {
            "created_at": ANY_DATETIME_STR,
            "name": "Bob",
            "widgets": 23,
        }
    }

and the assertion will do what you mean.

.. _pytest: https://docs.pytest.org

Installation
============
``anys`` requires Python 3.6 or higher.  Just use `pip <https://pip.pypa.io>`_
for Python 3 (You have pip, right?) to install it::

    python3 -m pip install anys


API
===

``anys`` provides the following functions & constants for matching against
values meeting certain criteria.  Matching is performed by comparing a value
against an ``anys`` matcher with ``==``, either directly or as a result of
comparing two larger structures with ``==``.

If a comparison raises a ``TypeError`` or ``ValueError`` (say, because you
evaluated ``42 == any_match(r'\d+')``, which tries to match a regex against an
integer), the exception is suppressed, and the comparison evaluates to
``False``; all other exceptions are propagated out.

``anys`` matchers can be combined using the ``&`` operator to produce new
matchers that require both operands to succeed; for example, ``any_gt(23) &
any_lt(42)`` will match any number between 23 and 42, exclusive, and nothing
else.

``anys`` matchers can be combined using the ``|`` operator to produce new
matchers that require at least one of the operands to succeed; for example,
``ANY_INT | ANY_STR`` will match any value that is an ``int`` or a ``str``.

Functions
---------

Note that, unless stated otherwise, ``anys`` functions cannot take ``anys``
matchers as arguments.

.. code:: python

    any_contains(key: Any)

Returns a matcher that matches any value for which ``key in value`` is true.
If ``key`` is an ``anys`` matcher, ``value == any_contains(key)`` will instead
be evaluated by iterating through the elements of ``value`` and checking
whether any match ``key``.

.. code:: python

    any_fullmatch(pattern: Union[AnyStr, re.Pattern[AnyStr]])

Returns a matcher that matches any string ``s`` for which
``re.fullmatch(pattern, s)`` succeeds

.. code:: python

    any_func(func: Callable)

Returns a matcher that matches any value ``x`` for which ``func(x)`` is true.
If ``func(x)`` raises a ``TypeError`` or ``ValueError``, it will be suppressed,
and ``x == any_func(func)`` will evaluate to ``False``.  All other exceptions
are propagated out.

.. code:: python

    any_ge(bound: Any)

Returns a matcher that matches any value greater than or equal to ``bound``

.. code:: python

    any_gt(bound: Any)

Returns a matcher that matches any value greater than ``bound``

.. code:: python

    any_in(iterable: Iterable)

Returns a matcher that matches any value that equals or matches an element of
``iterable`` (which may contain ``anys`` matchers).  Note that, if ``iterable``
is a string, only individual characters in the string will match; to match
substrings, use ``any_substr()`` instead.

.. code:: python

    any_instance(classinfo)

Returns a matcher that matches any value that is an instance of ``classinfo``.
``classinfo`` can be either a type or a tuple of types (or, starting in Python
3.10, a ``Union`` of types).

A number of pre-composed ``any_instance()`` values are provided as constants
for your convenience; see "Constants_" below.

.. code:: python

    any_le(bound: Any)

Returns a matcher that matches any value less than or equal to ``bound``

.. code:: python

    any_lt(bound: Any)

Returns a matcher that matches any value less than ``bound``

.. code:: python

    any_match(pattern: Union[AnyStr, re.Pattern[AnyStr]])

Returns a matcher that matches any string ``s`` for which ``re.match(pattern,
s)`` succeeds

.. code:: python

    any_search(pattern: Union[AnyStr, re.Pattern[AnyStr]])

Returns a matcher that matches any string ``s`` for which ``re.search(pattern,
s)`` succeeds

.. code:: python

    any_substr(s: AnyStr)

Returns a matcher that matches any substring of ``s``

.. code:: python

    any_with_attrs(mapping: Mapping)

Returns a matcher that matches any object ``obj`` such that ``getattr(obj, k)
== v`` for all ``k,v`` in ``mapping.items()``.

The values (but not the keys) of ``mapping`` can be ``anys`` matchers.

.. code:: python

    any_with_entries(mapping: Mapping)

Returns a matcher that matches any object ``obj`` such that ``obj[k] == v`` for
all ``k,v`` in ``mapping.items()``.

The values (but not the keys) of ``mapping`` can be ``anys`` matchers.

.. code:: python

    maybe(arg: Any)

Returns a matcher that matches ``None`` and any value that equals or matches
``arg`` (which can be an ``anys`` matcher)

.. code:: python

    not_(arg: Any)

Returns a matcher that matches anything that does not equal or match ``arg``
(which can be an ``anys`` matcher)

Constants
---------

The following constants match values of the given type:

- ``ANY_BOOL``
- ``ANY_BYTES``
- ``ANY_COMPLEX``
- ``ANY_DATE`` — Matches ``date`` instances.  You may not be aware, but
  ``datetime`` is a subclass of ``date``, and so this also matches
  ``datetime``\s.  If you only want to match actual ``date``\s, use
  ``ANY_STRICT_DATE``.
- ``ANY_DATETIME``
- ``ANY_DICT``
- ``ANY_FLOAT``
- ``ANY_INT``
- ``ANY_ITERABLE``
- ``ANY_ITERATOR``
- ``ANY_LIST``
- ``ANY_MAPPING``
- ``ANY_NUMBER``
- ``ANY_SEQUENCE``
- ``ANY_SET``
- ``ANY_STR``
- ``ANY_STRICT_DATE`` — Matches any instance of ``date`` that is not an
  instance of ``datetime``
- ``ANY_TUPLE``

The following constants match `aware or naïve`__ ``datetime`` or ``time``
values:

__ https://docs.python.org/3/library/datetime.html#aware-and-naive-objects

- ``ANY_AWARE_DATETIME``
- ``ANY_AWARE_TIME``
- ``ANY_NAIVE_DATETIME``
- ``ANY_NAIVE_TIME``

The following constants match ISO 8601-style date, time, & datetime strings.
"Aware" matchers require timezone information, while "naïve" matchers forbid
it.

- ``ANY_AWARE_DATETIME_STR``
- ``ANY_AWARE_TIME_STR``
- ``ANY_DATETIME_STR``
- ``ANY_DATE_STR``
- ``ANY_NAIVE_DATETIME_STR``
- ``ANY_NAIVE_TIME_STR``
- ``ANY_TIME_STR``

Other constants:

- ``ANY_FALSY`` — Matches anything considered false
- ``ANY_TRUTHY`` — Matches anything considered true

Caveat: Custom Classes
======================

When a well-behaved class defines an ``__eq__`` method, it will only test
against values of the same class, returning ``NotImplemented`` for other types,
[1]_ which signals Python to evaluate ``x == y`` by instead calling ``y``'s
``__eq__`` method.  Thus, when comparing an ``anys`` matcher against an
instance of a well-behaved class, the matcher can be on either the left or the
right of the ``==``.  All of the classes in the Python standard library are
well-behaved, as are classes that don't define ``__eq__`` methods, but some
custom classes in third-party code are not well-behaved.  In order to
successfully compare an ``anys`` matcher against an ill-behaved class, the
matcher must be on the **left** side of the ``==`` operator; if it is on the
right, only the custom class's ``__eq__`` method will be consulted, which
usually means that the comparison will always evaluate to false.

.. [1] In order to work their magic, ``anys`` matchers do not follow this rule,
       and so they are not well-behaved.  "Do as I say, not as I do," as they
       say.
