import numpy as np

def q_learning_update(Q, s, a, r, s_next, alpha, gamma):
    """
    Returns: updated Q-table Q_new
    """
    # Write code here
    Q = np.array(Q, dtype=float)
    Q_new = Q.copy()

    current_q = Q[s, a]
    best_next_q = np.max(Q[s_next])

    Q_new[s, a] = current_q + alpha * (
        r + gamma * best_next_q - current_q
    )

    return Q_new
    pass