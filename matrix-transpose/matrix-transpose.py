import numpy as np

def matrix_transpose(A):
    rows = len(A)
    cols = len(A[0])

    At = [[0 for _ in range(rows)] for _ in range(cols)]
    for i in range(rows):
          for j in range(cols):
                At[j][i] = A[i][j]
    
    return np.array(At)
    pass
