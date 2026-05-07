import numpy as np

def huber_loss(y_true, y_pred, delta=1.0):
    """
    Compute Huber Loss for regression.
    """
    # Write code here
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    e = y_true - y_pred
    e = np.where(abs(e) > delta, delta * (abs(e) - delta / 2), e ** 2 / 2)
    return np.mean(e)
    
    pass