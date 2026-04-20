def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    cnt = 0
    for i in range(k):
        if recommended[i] in relevant:
            cnt += 1
    result = []
    result.append(cnt / k)
    result.append(cnt / len(relevant))
    return result