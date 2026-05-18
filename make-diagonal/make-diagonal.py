import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    # Write code here
    matrix = np.zeros((len(v) , len(v)))
    index = 0
    for i in range(len(matrix)):         
        for j in range(len(matrix[0])):  
            if i == j:
                matrix[i][j] = v[index]
                index += 1

    return matrix
    pass
