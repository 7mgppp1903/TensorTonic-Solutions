import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    rows = len(A)
    cols = len(A[0])
    sum = 0
    for i in range(rows):
        for j in range(cols):
            if i == j:
                sum += A[i][j]
    return sum
    pass
