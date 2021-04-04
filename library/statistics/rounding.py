from library.errors.scalars import allow_none_scalar, positive_integer

def rounded_value(number, precision):
    """
    Rounds a number to a certain decimal place, but returns a non-zero result if the number being rounded is non-zero even if it would round to zero at that level of decimal precision; allows None as a possible input

    Parameters
    ----------
    number : int or float
        Number to round
    precision : int
        Maximum number of digits that can appear after the decimal place of the result

    Raises
    ------
    TypeError
        First argument must be an integer, a float, or None
    ValueError
        Last argument must be a positive integer

    Returns
    -------
    number : int or float
        Original number rounded to the number of decimal places indicated by the precision input

    Examples
    --------
    Round the number 9.2157823956916472 to four decimal places
        >>> number_normal = rounded_value(9.2157823956916472, 4)
        >>> print(number_normal)
        9.2158
    Round the number -0.00000003 to four decimal places
        >>> number_abnormal = rounded_value(-0.00000003, 4)
        >>> print(number_abnormal)
        -0.0001
    """
    allow_none_scalar(number)
    positive_integer(precision)
    if number == None:
        return None
    elif number < 10**(-precision) and number > 0:
        return 10**(-precision)
    elif number > -10**(-precision) and number < 0:
        return -10**(-precision)
    else:
        return round(number, precision)