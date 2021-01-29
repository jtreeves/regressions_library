from .maximum import maximum
from .minimum import minimum

def range(data):
    max_value = maximum(data)
    min_value = minimum(data)
    result = max_value - min_value
    return result