def residual(actual, expected):
    result = actual - expected
    return result

def residual_array(actual_array, expected_array):
    results = []
    for i in range(len(actual_array)):
        results.append(residual(actual_array[i], expected_array[i]))
    return results