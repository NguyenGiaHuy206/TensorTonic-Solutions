import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    # Write code here
    if len(y_pred) != len(y_true):
        return None
    y_pred = np.array(y_pred)
    y_true = np.array(y_true)
    loss = np.sum((y_pred - y_true) ** 2)
    MSE = loss / len(y_pred)
    return MSE
    pass
