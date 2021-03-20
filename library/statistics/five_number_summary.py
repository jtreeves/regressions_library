from .minimum import minimum
from .maximum import maximum
from .median import median
from .quartiles import quartiles

def five_number_summary(data):
    result = {
        'minimum': minimum(data),
        'q1': quartiles(data, 1),
        'median': median(data),
        'q3': quartiles(data, 3),
        'maximum': maximum(data)
    }
    return result