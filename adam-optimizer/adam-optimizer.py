import numpy as np
import math 
def adam_step(param, grad, m, v, t, lr=1e-3, beta1=0.9, beta2=0.999, eps=1e-8):
    """
    One Adam optimizer update step.
    Return (param_new, m_new, v_new).
    """
    # Write code here
    param_new = np.array(param)
    grad_new = np.array(grad)
    m_new = np.array(m)
    v_new = np.array(v)
    m_new = beta1*m_new + (1 - beta1)*grad_new
    v_new = beta2*v_new + (1 - beta2)*(grad_new**2)
    m_hat = m_new / (1 - beta1**t)
    v_hat = v_new / (1 - beta2**t)
    param_new = param_new - lr * (m_hat / (v_hat**0.5 + eps))
    return param_new, m_new, v_new
    pass