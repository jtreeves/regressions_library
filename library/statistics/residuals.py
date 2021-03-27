def single_residual(actual, expected):
    result = actual - expected
    return result

def multiple_residuals(actual_array, expected_array):
    results = []
    for i in range(len(actual_array)):
        results.append(single_residual(actual_array[i], expected_array[i]))
    return results