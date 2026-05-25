import numpy as np

def td_value_update(V, s, r, s_next, alpha, gamma):
    """
    Returns: updated value function V_new
    """
    # Write code here
    V_new = V.copy()
    td_target = r + gamma * V[s_next]
    td_error = td_target - V[s]
    V_new[s] = V[s] + alpha * td_error
    return V_new
    pass