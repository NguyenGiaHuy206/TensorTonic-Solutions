def remove_stopwords(tokens, stopwords):
    """
    Returns: list[str] - tokens with stopwords removed (preserve order)
    """
    # Your code here
    output = [w for w in tokens if not w in stopwords]
    return output
    pass