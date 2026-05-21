import numpy as np

def compute_advantage(states, rewards, V, gamma):
    """
    Returns: A (NumPy array of advantages)
    """
    # Write code here
    G = np.zeros(len(rewards))
    advantages = np.zeros(len(rewards))
    running_return = 0
    
    for t in reversed(range(len(rewards))):
        running_return = rewards[t] + gamma * running_return
        G[t] = running_return
        advantages[t] = G[t] - V[states[t]]
    
    return advantages
    pass
