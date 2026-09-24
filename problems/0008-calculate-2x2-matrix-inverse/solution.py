def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.
    
    Args:
        matrix: A 2x2 matrix represented as [[a, b], [c, d]]
    
    Returns:
        The inverse matrix as a 2x2 list, or None if the matrix is singular
        (i.e., determinant equals zero)
    """
    # Your code here
    det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    if det == 0 or len(matrix) != len(matrix[0]) != 2: 
        return None

    inverse_matrix = [[float(matrix[1][1]), float(-matrix[0][1])],
                      [float(-matrix[1][0]), float(matrix[0][0])]]



    for i in inverse_matrix:
        i[0] *= (1/det)
        i[1] *= (1/det)

    return inverse_matrix



