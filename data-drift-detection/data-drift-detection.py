def detect_drift(reference_counts, production_counts, threshold):
    """
    Compare reference and production distributions to detect data drift.
    """
    # Write code here
    result = {}
    pref_rc = sum(reference_counts)
    pref_pc = sum(production_counts)
    for i in range(len(reference_counts)):
        reference_counts[i] /= pref_rc
        production_counts[i] /= pref_pc 
    sum_tvd = 0
    for i in range(len(reference_counts)):
        sum_tvd += abs(reference_counts[i] - production_counts[i])
    tvd = sum_tvd / 2
    if tvd > threshold:
        result["score"] = tvd
        result["drift_detected"] = True
    else:
        result["score"] = tvd
        result["drift_detected"] = False

    return result
    pass