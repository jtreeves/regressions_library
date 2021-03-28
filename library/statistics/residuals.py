from library.errors.scalars import scalar_value
from library.errors.vectors import compare_vectors

def single_residual(actual, expected):
    scalar_value(actual, 'first')
    scalar_value(expected, 'second')
    result = actual - expected
    return result

def multiple_residuals(actual_array, expected_array):
    compare_vectors(actual_array, expected_array)
    results = []
    for i in range(len(actual_array)):
        results.append(single_residual(actual_array[i], expected_array[i]))
    return results