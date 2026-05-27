import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    # Write code here
    X = np.asarray(X)
    if X.shape[0] < 2 or X.ndim != 2:
        return None
    m = np.mean(X, axis = 0)
    X_centered = X - m
    Covariance_matrix = (1 / (X.shape[0] - 1)) * X_centered.T @ X_centered
    return Covariance_matrix
    pass