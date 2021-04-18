from library.errors.vectors import allow_none_vector

def separate_elements(vector):
    allow_none_vector(vector)
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