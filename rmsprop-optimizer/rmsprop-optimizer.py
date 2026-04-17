import numpy as np

def rmsprop_step(w, g, s, lr=0.001, beta=0.9, eps=1e-8):
    """
    Perform one RMSProp update step.
    """
    w_new = np.array(w)
    g_new = np.array(g)
    s_new = np.array(s)
    s_new = beta * s_new + (1 - beta) * (g_new ** 2)
    w_new = w_new  - (lr / (s_new + eps) ** 0.5) * g_new
    return w_new, s_new
    # Write code here
    pass