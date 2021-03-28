def first_scalar(scalar):
    if not isinstance(scalar, (int, float)):
        raise TypeError('First argument must be an integer or float')

def last_scalar(scalar):
    if not isinstance(scalar, (int, float)):
        raise TypeError('Last argument must be an integer or float')

def integer(scalar):
    if not isinstance(scalar, int):
        raise TypeError('Last argument must be an integer')