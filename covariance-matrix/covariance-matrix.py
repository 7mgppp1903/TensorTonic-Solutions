import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    # Write code here
    
    X = np.array(X, float)
    if X.ndim != 2:
        return None
    N = X.shape[0]
    mu = np.mean(X, axis = 0);
    Xcent = X - mu
    if N <= 1:
        return None
    cov = (1/(N - 1)) *  np.dot(Xcent.T, Xcent)

    return cov
    
    pass