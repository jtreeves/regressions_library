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
    number : float
        Original number rounded to the number of decimal places indicated by the precision input

    See Also
    --------
    :func:`~library.statistics.sort.sorted_list`, :func:`~library.statistics.summation.sum_value`

    Notes
    -----
    - Number to round: :math:`n`
    - Absolute value of number: :math:`a = |n|`
    - Maximum number of digits after decimal place of result: :math:`d`
    - Check size of number: :math:`c(a,d) = \\lfloor a\\cdot{10^d} \\rfloor`
    - Significant digit: :math:`s(a,d) = \\lfloor ( a\\cdot{10^d} - \\lfloor a\\cdot{10^d} \\rfloor )\\cdot{10} \\rfloor`
    - If :math:`c(a,d) = 0`:
        
        - Rounding formula (if :math:`n = 0`): :math:`r = 0`
        - If :math:`n \\neq 0`:

            - Rounding formula (if :math:`a = n`): :math:`r(d) = 10^{-d}`
            - Rounding formula (if :math:`a \\neq n`): :math:`r(d) = -10^{-d}`
    
    - If :math:`c(a,d) \\neq 0`:

        - If :math:`a = n`:
        
            - Rounding formula (if :math:`s(a,d) \\geq 5`): :math:`r(a,d) = \\frac{\\lceil a\\cdot{10^d} \\rceil}{10^d}`
            - Rounding formula (if :math:`s(a,d) < 5`): :math:`r(a,d) = \\frac{\\lfloor a\\cdot{10^d} \\rfloor}{10^d}`
        
        - If :math:`a \\neq n`:
        
            - Rounding formula (if :math:`s(a,d) \\geq 5`): :math:`r(a,d) = -\\frac{\\lceil a\\cdot{10^d} \\rceil}{10^d}`
            - Rounding formula (if :math:`s(a,d) < 5`): :math:`r(a,d) = -\\frac{\\lfloor a\\cdot{10^d} \\rfloor}{10^d}`
    
    - |rounding|

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
        return float(round(number, precision))