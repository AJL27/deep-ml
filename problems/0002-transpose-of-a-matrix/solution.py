def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here

    m = len(a)
    n = len(a[0])

    output_matrix = [[] for _ in range(n)]

    for i in range(m): #column -> row
        for j in range(n): #row -> column
            output_matrix[j].append(a[i][j])

    return output_matrix
            
