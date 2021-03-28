from library.errors.scalars import allow_none_scalar, positive_integer

def rounded_value(number, precision):
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