def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    # Your code here
    word_counts = {}

    for sentence in sentences:
        for word in sentence:
            word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts
    pass