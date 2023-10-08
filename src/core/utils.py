def float_to_integer(price_in_float, currency_factor=100):
    """
    The function `float_to_integer` converts a price from float to integer by multiplying it with
    a currency factor and rounding it to the nearest whole number.

    :param price_in_float: The price in float is the original price that you want to convert to an
    integer. It can be any decimal number representing a price
    :param currency_factor: The currency_factor parameter is used to convert the price from a float to
    an integer by multiplying it. By default, it is set to 100, which means that the price will be
    multiplied by 100 to convert it to cents, defaults to 100 (optional)
    Adjust the currency_factor based on your currency's smallest unit.
    For example, for Japanese yen, where 1 yen is the smallest unit, you would set currency_factor to 1.

    :return: the price as an integer, after converting it from a float and rounding it to the nearest
    whole number.
    """

    price_in_cents = round(price_in_float * currency_factor)
    price_in_integer = int(price_in_cents)

    return price_in_integer


def integer_to_float(price_in_integer, currency_factor=100):
    """
    The function converts an integer price to a float by dividing it by a currency factor.
    
    :param price_in_integer: The price in integer format that you want to convert to float. This is the
    original price value before converting it to a different currency or format
    :param currency_factor: The currency_factor is a value that represents the conversion rate from the
    integer currency to the float currency. It is used to divide the price_in_integer to convert it into
    a float value. By default, the currency_factor is set to 100, which means that the price_in_integer
    is assumed to be, defaults to 100 (optional)
    :return: the price_in_float, which is the price in float format after dividing the price_in_integer
    by the currency_factor.
    """
    price_in_float = float(price_in_integer) / currency_factor

    return price_in_float
