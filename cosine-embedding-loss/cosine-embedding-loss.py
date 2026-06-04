import numpy as np
def cosine_embedding_loss(x1, x2, label, margin):
    """
    Compute cosine embedding loss for a pair of vectors.
    """
    # Write code here
    x1 = np.array(x1, dtype=float)
    x2 = np.array(x2, dtype=float)

    dot = np.dot(x1, x2)
    norm1 = np.linalg.norm(x1)
    norm2 = np.linalg.norm(x2)

    # tránh chia 0
    if norm1 == 0 or norm2 == 0:
        cos = 0.0
    else:
        cos = dot / (norm1 * norm2)

    if label == 1:
        loss = 1 - cos
    else:  # label == -1
        loss = max(0.0, cos - margin)

    return loss