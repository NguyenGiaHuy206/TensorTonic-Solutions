import numpy as np
from collections import Counter
def cohens_kappa(rater1, rater2):
    """
    Compute Cohen's Kappa coefficient.
    """
    # Write code here
    rater1 = np.array(rater1)
    rater2 = np.array(rater2)
    n = len(rater1)
    if n == 0:
        return 1.0

    po = np.sum(rater1 == rater2) / n

    count1 = Counter(rater1)
    count2 = Counter(rater2)

    labels = set(count1.keys()) | set(count2.keys())
    pe = 0.0
    for label in labels:
        pe += (count1[label] / n) * (count2[label] / n)

    if abs(1 - pe) < 1e-12:
        return 1.0
    kappa = (po - pe) / (1 - pe)
    return float(kappa)
    pass