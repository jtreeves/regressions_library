from library.errors.scalars import first_scalar, last_scalar
from library.errors.vectors import compare_vectors

def single_residual(actual, expected):
    first_scalar(actual)
    last_scalar(expected)
    result = actual - expected
    return result

def multiple_residuals(actual_array, expected_array):
    compare_vectors(actual_array, expected_array)
    results = []
    for i in range(len(actual_array)):
        results.append(single_residual(actual_array[i], expected_array[i]))
    return results