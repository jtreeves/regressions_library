from numpy import matrix
from numpy.linalg import inv
from library.errors.matrices import compare_rows
from library.errors.scalars import positive_integer
from library.statistics.rounding import rounded_value
from library.vectors.dimension import single_dimension
from .multiplication import matrix_product
from .transpose import adjugate

def system_solution(matrix_one, matrix_two, precision):
    """
    Solves a system of equations using matrices (independent matrix multiplied by resultant matrix equals dependent matrix)

    Parameters
    ----------
    matrix_one : list or tuple
        List of lists of numbers representing the independent matrix of a system of equations
    matrix_two : list or tuple
        List of lists of numbers representing the dependent matrix of a system of equations
    precision : int
        Maximum number of digits that can appear after the decimal place of the results

    Raises
    ------
    TypeError
        First and second arguments must be 2-dimensional lists or tuples
    TypeError
        Elements nested within first and second arguments must be integers or floats
    ValueError
        First and second arguments must contain the same amount of lists
    ValueError
        Last argument must be a positive integer
    
    Returns
    -------
    solution : list
        Row vector of coefficients that if expressed as a column vector would satisfy the equation

    Examples
    --------
    Solve the system that has an independent matrix of [[2, 3], [1, -1]] and a dependent matrix of [[5], [1]] (and round the results to four decimal places)
        >>> solution_2values = system_solution([[2, 3], [1, -1]], [[5], [1]], 4)
        >>> print(solution_2values)
        [1.6, 0.6]
    Solve the system that has an independent matrix of [[1, -2, 3], [-4, 5, -6], [7, -8, 9], [-10, 11, 12]] and a dependent matrix of [[2], [-3], [5], [-7]] (and round the results to four decimal places)
        >>> solution_3values = system_solution([[1, -2, 3], [-4, 5, -6], [7, -8, 9], [-10, 11, 12]], [[2], [-3], [5], [-7]], 4)
        >>> print(solution_3values)
        [-0.8611, -1.3889, -0.0278]
    """
    compare_rows(matrix_one, matrix_two)
    positive_integer(precision)
    transposition = adjugate(matrix_one)
    product = matrix_product(transposition, matrix_one)
    product_matrix = matrix(product, dtype='float')
    inversion = inv(product_matrix)
    inversion_list = matrix.tolist(inversion)
    second_product = matrix_product(inversion_list, transposition)
    solution_column = matrix_product(second_product, matrix_two)
    solution = single_dimension(solution_column, 1)
    result = []
    for number in solution:
        result.append(rounded_value(number, precision))
    return result