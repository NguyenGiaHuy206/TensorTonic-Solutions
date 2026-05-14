import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    # Write code here
    percentiles = np.percentile(x, q, method = "linear")
    percentiles = np.array(percentiles)
    return np.sort(percentiles)
    pass