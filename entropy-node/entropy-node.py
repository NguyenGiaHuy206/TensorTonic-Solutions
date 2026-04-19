import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
   
    u, counts = np.unique(y, return_counts=True)
    if len(u) <= 1:
        return float(0)

    result = 0.0
    p = 1 / (len(y))
    for i in range(len(u)):
        p_i = counts[i] * p
        result += -(p_i) * np.log2(p_i)
    return float(result)
    pass