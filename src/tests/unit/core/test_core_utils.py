from apps.core.utils import float_to_integer, integer_to_float


def test_float_to_integer_with_default_currency():
    assert float_to_integer(19.99) == 1999


def test_integer_to_float():
    assert integer_to_float(1999) == 19.99
