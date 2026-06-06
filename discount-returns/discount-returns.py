def discount_returns(rewards, gamma):
    """
    Compute the discounted return at every timestep.
    """
    # Write code here
    n = len(rewards)
    returns = [0] * n

    G = 0
    for t in reversed(range(n)):
        G = rewards[t] + gamma * G
        returns[t] = G

    return returns