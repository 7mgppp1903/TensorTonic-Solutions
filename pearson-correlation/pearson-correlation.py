import numpy as np

def pearson_correlation(X):
    try:
        X = np.array(X, dtype=float)

        if X.ndim != 2:
            return None

        N = X.shape[0]
        if N <= 1:
            return None

        mu = np.mean(X, axis=0)
        Xcent = X - mu

        cov = (1 / (N - 1)) * (Xcent.T @ Xcent)

        std = np.sqrt(np.diag(cov))
        denom = np.outer(std, std)

        corr = cov / denom  

        return corr

    except:
        return None