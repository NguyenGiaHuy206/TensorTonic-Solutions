def promote_model(models):
    """
    Decide which model version to promote to production.
    """
    # Write code here
    best = max(models,key=lambda x: (x['accuracy'],-x['latency'],x['timestamp']))
    return best['name']
    pass