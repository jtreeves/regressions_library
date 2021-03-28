def scalar_value(scalar, position):
    identifier = ''
    argument = 'argument'
    if position == 'only':
        identifier = argument
    else:
        identifier = position + ' ' + argument
    if not isinstance(scalar, (int, float)):
        raise TypeError(f'{identifier.capitalize()} must be an integer or float')

def two_scalars(scalar_one, scalar_two):
    scalar_value(scalar_one, 'first')
    scalar_value(scalar_two, 'second')

def three_scalars(scalar_one, scalar_two, scalar_three):
    two_scalars(scalar_one, scalar_two)
    scalar_value(scalar_three, 'third')

def four_scalars(scalar_one, scalar_two, scalar_three, scalar_four):
    three_scalars(scalar_one, scalar_two, scalar_three)
    scalar_value(scalar_four, 'fourth')

def compare_scalars(scalar_two, scalar_three):
    scalar_value(scalar_two, 'second')
    scalar_value(scalar_three, 'third')
    if scalar_two >= scalar_three:
        raise ValueError('Second argument must be less than third argument')

def positive_integer(scalar):
    if not isinstance(scalar, int) or not scalar > 0:
        raise TypeError('Last argument must be a positive integer')

def select_integers(scalar, choices):
    if scalar not in choices:
        raise ValueError(f'Second argument must be one of the following integers: {choices}')