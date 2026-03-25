import numpy as np

def calculate_eigenvalues(matrix):
    try:
        matrix = np.array(matrix, float)


        if matrix.ndim != 2:
            return None

        if matrix.shape[0] != matrix.shape[1]:
            return None

        eigenvalues = np.linalg.eigvals(matrix)

        return eigenvalues

    except:
        return None