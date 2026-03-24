import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    # Write code here
    n = len(v)
    Diag = np.zeros((n,n))

    for i in range (n):
        Diag[i][i] = v[i]

    return Diag
    
    
    pass
