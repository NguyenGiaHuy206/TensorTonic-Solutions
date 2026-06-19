def value_iteration_step(values, transitions, rewards, gamma):
    """
    Perform one step of value iteration and return updated values.
    """
    # Write code here
    n_states = len(values)
    new_values = []

    for s in range(n_states):
        action_values = []

        for a in range(len(transitions[s])):
            expected_future = 0.0

            for s_next in range(n_states):
                expected_future += (
                    transitions[s][a][s_next] * values[s_next]
                )

            q = rewards[s][a] + gamma * expected_future
            action_values.append(q)

        new_values.append(max(action_values))

    return new_values