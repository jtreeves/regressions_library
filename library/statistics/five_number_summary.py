from .minimum import minimum
from .maximum import maximum
from .median import median
from .quartiles import quartiles
from .rounding import rounding

def five_number_summary(data, precision):
    min_value = minimum(data)
    rounded_min = rounding(min_value, precision)
    max_value = maximum(data)
    rounded_max = rounding(max_value, precision)
    q1 = quartiles(data, 1)
    rounded_q1 = rounding(q1, precision)
    q3 = quartiles(data, 3)
    rounded_q3 = rounding(q3, precision)
    median_value = median(data)
    rounded_med = rounding(median_value, precision)
    result = {
        'minimum': rounded_min,
        'q1': rounded_q1,
        'median': rounded_med,
        'q3': rounded_q3,
        'maximum': rounded_max
    }
    return result