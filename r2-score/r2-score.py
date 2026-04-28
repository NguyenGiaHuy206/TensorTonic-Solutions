import numpy as np

def r2_score(y_true, y_pred) -> float:
    """
    Compute R² (coefficient of determination) for 1D regression.
    Handle the constant-target edge case:
      - return 1.0 if predictions match exactly,
      - else 0.0.
    """
    
    # Write code here
    y_pred = np.array(y_pred)
    y_true = np.array(y_true)
    if np.all(y_true == y_pred):
        return 1.0

    if np.mean(y_true) == 1:
        return 0.0
    SSres = np.sum((y_true - y_pred) ** 2)
    SStot = np.sum((y_true - np.mean(y_true)) ** 2)
    return 1 - SSres / SStot

    pass