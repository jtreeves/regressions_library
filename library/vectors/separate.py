def separate_elements(vector):
    numerical_elements = []
    other_elements = []
    for element in vector:
        if isinstance(element, (int, float)):
            numerical_elements.append(element)
        else:
            other_elements.append(element)
    results = {
        'numerical': numerical_elements,
        'other': other_elements
    }
    return results