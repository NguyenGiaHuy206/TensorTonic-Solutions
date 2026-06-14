import numpy as np

def dropout(x, p=0.5, rng=None):
    """
    Apply dropout to input x with probability p.
    Return (output, dropout_pattern).
    """
    # Write code here
    x = np.asarray(x, dtype=float)
    if rng is not None:
        rand = rng.random(x.shape)
    else:
        rand = np.random.random(x.shape)
    keep_prob = 1 - p
    dropout_pattern = np.where(
        rand < keep_prob,
        1.0 / keep_prob,
        0.0
    )
    output = x * dropout_pattern
    return output, dropout_pattern
    pass