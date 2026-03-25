import numpy as np

def matrix_inverse(A):
    """
    Returns: A_inv of shape (n, n) such that A @ A_inv ≈ I
    """
    # Write code here
    A = np.array(A, float)

    if A.ndim != 2:
        return None

    if A.shape[0] != A.shape[1]:
        return None

    if np.linalg.det(A) == 0:
        return None

    inverse = np.linalg.inv(A)

    return inverse
    pass
