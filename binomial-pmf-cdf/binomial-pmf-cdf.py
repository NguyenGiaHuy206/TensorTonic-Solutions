import numpy as np
from scipy.special import comb

def binomial_pmf_cdf(n, p, k):
    """
    Compute Binomial PMF and CDF.
    """
    # Write code here
    combinations = comb(n, k, exact=False)
    pmf = combinations * (p**k) * ((1 - p)**(n - k))
    cdf = 0
    for i in range(k + 1):
        combinations = comb(n, i, exact=False)
        cdf += combinations * (p ** i) * ((1 - p) ** (n - i))

    return pmf, cdf
    pass