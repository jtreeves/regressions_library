from .minimum import minimum_value
from .maximum import maximum_value
from .median import median_value
from .quartiles import quartile_value
from .rounding import rounded_value

def five_number_summary(data, precision):
    min_value = minimum_value(data)
    rounded_min = rounded_value(min_value, precision)
    max_value = maximum_value(data)
    rounded_max = rounded_value(max_value, precision)
    q1 = quartile_value(data, 1)
    rounded_q1 = rounded_value(q1, precision)
    q3 = quartile_value(data, 3)
    rounded_q3 = rounded_value(q3, precision)
    median = median_value(data)
    rounded_med = rounded_value(median, precision)
    result = {
        'minimum': rounded_min,
        'q1': rounded_q1,
        'median': rounded_med,
        'q3': rounded_q3,
        'maximum': rounded_max
    }
    return result