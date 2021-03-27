from .maximum import maximum_value
from .minimum import minimum_value

def range_value(data):
    max_value = maximum_value(data)
    min_value = minimum_value(data)
    result = max_value - min_value
    return result