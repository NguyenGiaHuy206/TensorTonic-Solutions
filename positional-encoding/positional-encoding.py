import numpy as np

def positional_encoding(seq_len, d_model, base=10000.0):
    """
    Return PE of shape (seq_len, d_model) using sin/cos formulation.
    Odd d_model -> last column is sin.
    """
    # Write code here
    positions = np.arange(seq_len).reshape(-1, 1)  # (seq_len, 1)

    pe = np.zeros((seq_len, d_model))

    even_idx = np.arange(0, d_model, 2)
    div_term = base ** (even_idx / d_model)

    angles = positions / div_term

    pe[:, 0::2] = np.sin(angles)

    if d_model > 1:
        pe[:, 1::2] = np.cos(angles[:, :pe[:, 1::2].shape[1]])

    return pe
    pass