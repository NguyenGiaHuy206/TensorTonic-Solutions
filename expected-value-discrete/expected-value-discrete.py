import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    ex_val = 0
    if sum(p) != 1:
        raise ValueError("Probabilities must sum to 1")
    for i in range(len(x)):
        ex_val += x[i] * p[i]
    return float(ex_val)
    pass
