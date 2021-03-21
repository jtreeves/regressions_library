def rounding(number, precision):
    if not number:
        return None
    elif number < 10**(-precision) and number > 0:
        return 10**(-precision)
    elif number > -10**(-precision) and number < 0:
        return -10**(-precision)
    else:
        return round(number, precision)