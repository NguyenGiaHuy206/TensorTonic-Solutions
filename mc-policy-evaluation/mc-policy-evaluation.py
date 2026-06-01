import numpy as np

def mc_policy_evaluation(episodes, gamma, n_states):
    """
    Returns: V (NumPy array of shape (n_states,))
    """
    # Write code here
    returns = [[] for _ in range(n_states)]

    for episode in episodes:
        G = 0.0
        returns_episode = [0.0] * len(episode)

        for t in range(len(episode) - 1, -1, -1):
            state, reward = episode[t]
            G = reward + gamma * G
            returns_episode[t] = G

        visited = set()

        for t, (state, _) in enumerate(episode):
            if state not in visited:
                visited.add(state)
                returns[state].append(returns_episode[t])

    V = np.zeros(n_states)

    for s in range(n_states):
        if returns[s]:
            V[s] = np.mean(returns[s])

    return V
    pass
