def first_scalar(scalar):
    if not isinstance(scalar, (int, float)):
        raise TypeError('First argument must be an integer or float')

def last_scalar(scalar):
    if not isinstance(scalar, (int, float)):
        raise TypeError('Last argument must be an integer or float')

def two_scalars(scalar_one, scalar_two):
    first_scalar(scalar_one)
    if not isinstance(scalar_two, (int, float)):
        raise TypeError('Second argument must be an integer or float')

def three_scalars(scalar_one, scalar_two, scalar_three):
    two_scalars(scalar_one, scalar_two)
    if not isinstance(scalar_three, (int, float)):
        raise TypeError('Third argument must be an integer or float')

def four_scalars(scalar_one, scalar_two, scalar_three, scalar_four):
    three_scalars(scalar_one, scalar_two, scalar_three)
    if not isinstance(scalar_four, (int, float)):
        raise TypeError('Fourth argument must be an integer or float')

def integer(scalar):
    if not isinstance(scalar, int):
        raise TypeError('Last argument must be an integer')