from library.errors.vectors import allow_none_vector

def separate_elements(vector):
    # Handle input errors
    allow_none_vector(vector)

    # Create lists to store separate values
    numerical_elements = []
    other_elements = []

    # Iterate over input
    for element in vector:
        # Store numerical elements
        if isinstance(element, (int, float)):
            numerical_elements.append(element)
        
        # Store non-numerical elements
        else:
            other_elements.append(element)
    
    # Package both types of element in single dictionary to return
    results = {
        'numerical': numerical_elements,
        'other': other_elements
    }
    return results